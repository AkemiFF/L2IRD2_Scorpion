from django.http import HttpResponse
from django.shortcuts import render, redirect
from UserPart.models import Problem, Subject,Keyword


def ViewInfo(request,problem_id):
    problem = Problem.objects.get(id=problem_id)
    context = {"title": "Responsable", "problem": problem}

    return render(request, "ViewInfo.html", context)


def back(request):
    problems = Problem.objects.all()
    subjects = Subject.objects.all()
    keyword = Keyword.objects.all()
    context = {"title": "Responsable", "problems": problems, "subjects": subjects, "keyword": keyword}

    return render(request, "BackOffice.html", context)


def feedback(request, problem_id):
    problems = Problem.objects.all()
    context = {"title": "Responsable", "problems": problems}
    problem = Problem.objects.get(id=problem_id)
    problem.changer_etat_en_cours()
    return render(request, "BackOffice.html", context)


def cloturer(request, problem_id):
    problems = Problem.objects.all()
    context = {"title": "Responsable", "problems": problems}
    problem = Problem.objects.get(id=problem_id)
    problem.changer_etat_termine()
    return render(request, "BackOffice.html", context)



