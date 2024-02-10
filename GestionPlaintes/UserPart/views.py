from django.shortcuts import render


def index(request):
    return render(request, 'acceuil.html')


def probleme(request):
    return render(request, 'probleme.html')