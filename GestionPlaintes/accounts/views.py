from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout, login
from .models import StatusUser


def index(request):
    if request.user.is_authenticated:
        return redirect('acceuil/')
    else:
        x = condition_acceuil(request)
        return x


def logout_view(request):
    logout(request)
    return redirect("page_1")


def condition_acceuil(request):
    if request.method == 'POST':
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                try:
                    status_user = StatusUser.objects.get(user=user)
                    status_user.status = True
                    status_user.save()
                except StatusUser.DoesNotExist:
                    StatusUser.objects.create(user=user, status=True)
                login(request, user)
                return redirect('acceuil/')
            else:
                error_message = "Adresse e-mail ou mot de passe incorrect."
                return render(request, 'index.html', {'error_message': error_message})
    elif 'email-inscrip' in request.POST and 'password-inscrip' in request.POST:
        email = request.POST['email-inscrip']
        password = request.POST['password-inscrip']
        first_name = request.POST.get('surname', '')
        last_name = request.POST.get('name', '')

        User = get_user_model()
        try:
            existing_user = User.objects.get(email=email)
            error_message = "L'utilisateur existe déjà."
            return render(request, 'index.html', {'error_message': error_message})
        except User.DoesNotExist:
            with transaction.atomic():
                user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                last_name=last_name)
                return redirect('acceuil')
    return render(request, 'index.html')