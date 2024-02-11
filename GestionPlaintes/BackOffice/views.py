from django.shortcuts import render, redirect
from UserPart.models import Problem


def back(request):
    problems = Problem.objects.all()
    context = {"title": "Responsable", "problems": problems}

    return render(request, "BackOffice.html", context)
