from django.shortcuts import render, redirect
from .models import Problem, Subject, Suggestion
from BackOffice.models import Message
from django.contrib.auth.decorators import login_required


@login_required
def suggestion(request):
    suggestions = Suggestion.objects.all()
    user = request.user
    context = {"suggestions": suggestions, 'title': "Suggestion", "user": user}
    return render(request, 'suggestion.html', context)


def index(request):
    if request.user.is_authenticated:
        msg = "Bienvenue aux nouveaux adhérents"
        context = {"message_acceuil": msg, "title": "Acceuil"}
        return render(request, 'acceuil.html', context)
    else:
        return redirect("page_1")


def probleme(request):
    if request.user.is_authenticated:
        subjects = Subject.objects.all()
        added = False
        context = {"subjects": subjects, 'title': "Formulaire Problème", "added": added}
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

        titre = "Messagerie"
        user = request.user
        problems = Problem.objects.filter(user=user)
        messages = Message.objects.filter(user=user)
        context = {"title": titre, "messages": messages, "problems": problems}
        return render(request, 'messagerie.html', context)
    else:
        return redirect("page_1")
    
    
def delete_message(request, mess_id):
    message = Message.objects.get(id=mess_id)
    message.delete()
    return redirect('messagerie')
