from django.shortcuts import render

from .models import Problem


def index(request):
    return render(request, 'acceuil.html')


def probleme(request):
    if request.POST:
        nom = request.POST['nom']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'probleme.html')
    return render(request, 'probleme.html')


def suggestion(request):
    return render(request, 'suggestion.html')


def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')