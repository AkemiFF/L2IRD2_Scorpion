from django.shortcuts import render, redirect


def back(request):
    return render(request, "BackOffice.html")