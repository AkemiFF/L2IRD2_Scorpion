from django.shortcuts import render

from .models import Problem


def index(request):
    return render(request, 'acceuil.html')


def probleme(request):
    if request.method == 'POST':
        problem = Problem.create_from_request(request)
        return render(request, 'probleme.html', {'problem': problem})
    return render(request, 'probleme.html')


def suggestion(request):
    return render(request, 'suggestion.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')