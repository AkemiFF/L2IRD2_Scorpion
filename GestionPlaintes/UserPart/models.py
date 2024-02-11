from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='keywords')

    def __str__(self):
        return self.name


def create_default_subjects(sender, **kwargs):
    if Subject.objects.count() == 0:
        default_subjects = [
            {"name": "Administration", "keywords": ["taxation", "perception", "comptabilité", "administration", "finance", "bureaucratie"]},
            {"name": "Sécurité publique", "keywords": ["incendie", "sécurité civile", "police", "urgence", "sauvetage", "alerte"]},
            {"name": "Voirie et transport", "keywords": ["déneigement", "entretien des rues et routes", "transport", "mobilité", "route", "voie"]},
            {"name": "Traitement des eaux usées", "keywords": ["traitement des eaux", "assainissement", "eaux usées", "égouts", "canalisation"]},
            {"name": "Cueillette des déchets et recyclage", "keywords": ["recyclage", "déchets", "collecte des déchets", "tri", "poubelle", "recyclable"]},
            {"name": "Urbanisme", "keywords": ["urbanisme", "aménagement du territoire", "planification urbaine", "architecture", "zone"]},
            {"name": "Loisirs et culture", "keywords": ["loisirs", "culture", "événements", "arts", "sport", "divertissement"]},
        ]
        for subject_data in default_subjects:
            subject = Subject.objects.create(name=subject_data["name"])
            for keyword_name in subject_data["keywords"]:
                Keyword.objects.create(name=keyword_name, subject=subject)


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_default_subjects(sender)


class Problem(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    etat = models.CharField(max_length=200, default="En attente", blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', blank=True, null=True)
    importance = models.IntegerField(default=1)

    def __str__(self):
        return self.nom

    def changer_etat_en_cours(self):
        if self.etat != "Terminé":
            self.etat = "En cours"
        self.save()

    def changer_etat_termine(self):
        self.etat = "Terminé"
        self.save()


    @classmethod
    def create_from_request(cls, request):
        status = False
        nom = request.POST.get('name')
        email = request.POST.get('email')
        subject_id = request.POST.get('subject')
        description = request.POST.get('message')
        image = request.FILES.get('photo')

        if not nom:
            raise ValueError("Le champ 'nom' est requis.")

        problem = cls(
            nom=nom,
            email=email,
            subject_id=subject_id,
            description=description,
            etat="En attente",
            image=image,
        )
        importance = 1
        if subject_id and description:
            subject = Subject.objects.get(pk=subject_id)
            relevant_keywords = subject.keywords.filter(name__in=description.split())
            importance += relevant_keywords.count()

        problem.importance = importance
        problem.save()

        status = True
        return status
