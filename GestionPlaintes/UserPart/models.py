from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Suggestion(models.Model):
    text = models.TextField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


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
        create_suggestions()


def create_suggestions():
    taxation_subject = Subject.objects.get(name="Administration")
    securite_subject = Subject.objects.get(name="Sécurité publique")
    voirie_subject = Subject.objects.get(name="Voirie et transport")
    eaux_usees_subject = Subject.objects.get(name="Traitement des eaux usées")
    dechets_recyclage_subject = Subject.objects.get(name="Cueillette des déchets et recyclage")
    urbanisme_subject = Subject.objects.get(name="Urbanisme")
    loisirs_culture_subject = Subject.objects.get(name="Loisirs et culture")

    # Créer les instances de Suggestion avec les textes correspondants et le sujet associé
    Suggestion.objects.create(text="- Mise en place de systèmes de taxation plus transparents et simplifiés pour les citoyens et les entreprises.\n"
                                    "- Utilisation de technologies numériques pour faciliter la perception des impôts et la comptabilité.\n"
                                    "- Formation du personnel administratif pour une meilleure gestion des finances publiques.",
                              subject=taxation_subject)
    Suggestion.objects.create(text="- Renforcement des services d'incendie en investissant dans de nouveaux équipements et en augmentant les effectifs.\n"
                                    "- Mise en place de programmes de sensibilisation à la sécurité civile et de formation aux premiers secours pour les résidents.\n"
                                    "- Amélioration de la coordination entre les services d'urgence pour une réponse plus efficace aux situations de crise.",
                              subject=securite_subject)
    Suggestion.objects.create(text="- Planification efficace du déneigement en hiver en utilisant des prévisions météorologiques avancées.\n"
                                    "- Investissement dans la réparation et l'entretien régulier des routes pour éviter les dommages causés par les intempéries.\n"
                                    "- Promotion des modes de transport alternatifs tels que le covoiturage, le vélo et les transports en commun pour réduire la pression sur les routes.\n",
                              subject=voirie_subject)
    Suggestion.objects.create(text="- Modernisation des installations de traitement des eaux usées pour garantir une meilleure qualité de l'eau.\n"
                                    "- Sensibilisation à l'importance de réduire la pollution de l'eau et de préserver les ressources hydriques.\n"
                                    "- Développement de technologies de traitement des eaux plus durables et économiques.\n",
                              subject=eaux_usees_subject)
    Suggestion.objects.create(text=" - Mise en place de programmes de sensibilisation à la réduction des déchets et au recyclage.\n"
                                    "- Expansion des infrastructures de collecte sélective pour encourager le tri des déchets à la source.\n"
                                    "- Collaboration avec des entreprises locales pour développer des solutions de recyclage innovantes.\n",
                              subject=dechets_recyclage_subject)
    Suggestion.objects.create(text="- Planification urbaine intégrée pour promouvoir un développement durable et équilibré.\n"
                                    "- Création d'espaces verts et de parcs urbains pour améliorer la qualité de vie des résidents.\n"
                                    "- Promotion de la mixité sociale et économique dans les quartiers pour favoriser la cohésion sociale.\n",
                              subject=urbanisme_subject)
    Suggestion.objects.create(text="- Investissement dans des infrastructures culturelles telles que des musées, des théâtres et des centres artistiques.\n"
                                    "- Organisation d'événements culturels et artistiques pour dynamiser la vie communautaire.\n"
                                    "- Soutien aux initiatives locales visant à préserver et promouvoir le patrimoine culturel de la région.\n",
                              subject=loisirs_culture_subject)


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_default_subjects(sender)


User = get_user_model()


class Problem(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    etat = models.CharField(max_length=200, default="En attente", blank=False, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='img/', blank=True, null=True)
    importance = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='problems',null=False,blank=False)

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
        user = request.user
        if not nom:
            raise ValueError("Le champ 'nom' est requis.")

        problem = cls(
            nom=nom,
            email=email,
            subject_id=subject_id,
            description=description,
            etat="En attente",
            image=image,
            user=user
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


