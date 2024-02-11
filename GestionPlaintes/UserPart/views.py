from django.shortcuts import render, redirect

from .models import Problem, Subject


def index(request):
    if request.user.is_authenticated:
        return render(request, 'acceuil.html')
    else:
        return redirect("page_1")


def probleme(request):
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


def suggestion(request):
    return render(request, 'suggestion.html')


def messagerie(request):
    return render(request, 'messagerie.html')


def contact(request):
    return render(request, 'contact.html')