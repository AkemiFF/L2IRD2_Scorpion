from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


def create_default_subjects(sender, **kwargs):
    if Subject.objects.count() == 0:
        default_subjects = [
            "Administration",
            "Sécurité publique",
            "Voirie et transport",
            "Traitement des eaux usées",
            "Cueillette des déchets et recyclage",
            "Urbanisme",
            "Loisirs et culture"
        ]
        for subject_name in default_subjects:
            Subject.objects.create(name=subject_name)


@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_default_subjects(sender)


class Problem(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', blank=True, null=True)

    def __str__(self):
        return self.nom

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
            image=image
        )
        status = True
        problem.save()
        return status
