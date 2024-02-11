from django.shortcuts import render, redirect

from .models import Problem, Subject


def index(request):
    if request.user.is_authenticated:
        return render(request, 'acceuil.html')
    else:
        return redirect("page_1")


def probleme(request):
    subjects = Subject.objects.all()
    context = {"subjects": subjects}
    if request.method == 'POST':
        problem = Problem.create_from_request(request)

        return render(request, 'probleme.html', context)

    context['problem'] = Problem()
    return render(request, 'probleme.html', context)


def suggestion(request):
    return render(request, 'suggestion.html')


def messagerie(request):
    return render(request, 'messagerie.html')


def contact(request):
    return render(request, 'contact.html')