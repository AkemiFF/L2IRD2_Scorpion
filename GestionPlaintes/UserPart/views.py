from django.shortcuts import render, redirect
from .models import Problem, Subject
from BackOffice.models import Message
from django.contrib.auth.decorators import login_required


@login_required
def suggestion(request):
    subjects = Subject.objects.all()
    user = request.user
    context = {"subjects": subjects, 'title': "Scorpion", "user": user}
    return render(request, 'suggestion.html', context)


def index(request):
    if request.user.is_authenticated:
        msg = "Bienvenue à vous nouveau joueur"
        context = {"message_acceuil": msg}
        return render(request, 'acceuil.html', context)
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


def messagerie(request):
    if request.user.is_authenticated:
        titre = "Gestion Plaintes"
        user = request.user
        messages = Message.objects.filter(user=user)
        context = {"Title": titre, "messages": messages}
        return render(request, 'messagerie.html', context)
    else:
        return redirect("page_1")


def contact(request):
    return render(request, 'contact.html')