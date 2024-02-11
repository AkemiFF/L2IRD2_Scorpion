from django.db import models

from django.db import models
from django.contrib.auth.models import User
from UserPart.models import Problem
from GestionPlaintes import settings


class Message(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message to {self.user} regarding {self.problem}"
