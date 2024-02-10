from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
    return render(request, 'acceuil.html')
