from django.db import models


class Problem(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', blank=True, null=True)

    def __str__(self):
        return self.nom

    @classmethod
    def create_from_request(cls, request):
        nom = request.POST['nom']
        email = request.POST['email']
        sujet = request.POST['subject']
        description = request.POST['message']

        if 'image' in request.FILES:
            image = request.FILES['image']
            problem = cls(nom=nom, email=email, sujet=sujet, description=description, image=image)
        else:
            problem = cls(nom=nom, email=email, sujet=sujet, description=description)

        problem.save()
        return problem
