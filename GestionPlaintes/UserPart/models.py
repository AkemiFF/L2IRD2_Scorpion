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
