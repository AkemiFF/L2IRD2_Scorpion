from django.shortcuts import render, redirect
from .models import Problem, Subject
from BackOffice.models import Message


def index(request):
    if request.user.is_authenticated:
        return render(request, 'acceuil.html')
    else:
        return redirect("page_1")


def probleme(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        added = False
        context = {"subjects": subjects, 'title': "Scorpion", "added": added}
        if request.method == 'POST':
            problem = Problem.create_from_request(request)
            if problem:
                added = True
            context["added"] = added
            return render(request, 'probleme.html', context)

        return render(request, 'probleme.html', context)
    else:
        return redirect("page_1")


def suggestion(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects, 'title': "Scorpion"}
    return render(request, 'suggestion.html', context)


def messagerie(request):
    titre = "Gestion Plaintes"
    msg = Message.objects.all()
    context = {"Title": titre, "message": msg}
    return render(request, 'messagerie.html')


def contact(request):
    return render(request, 'contact.html')