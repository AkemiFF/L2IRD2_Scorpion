from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError


def index(request):
    if request.method == 'POST':
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']

        elif 'email-inscrip' in request.POST and 'password-inscrip' in request.POST:
            email = request.POST['email-inscrip']
            password = request.POST['password-inscrip']
            first_name = request.POST.get('surname', '')
            last_name = request.POST.get('name', '')

            User = get_user_model()
            try:
                existing_user = User.objects.get(email=email)
                return render(request, 'existing_user_error.html')
            except User.DoesNotExist:
                user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                last_name=last_name)
                return render(request, 'acceuil.html')

    return render(request, 'index.html')
