from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate


def index(request):
    if request.method == 'POST':
        if 'email' in request.POST and 'password' in request.POST:
            email = request.POST['email']
            password = request.POST['password']

            user = authenticate(request, email=email, password=password)
            if user is not None:
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
                user = User.objects.create_user(email=email, password=password, first_name=first_name,
                                                last_name=last_name)
                return render(request, 'acceuil.html')

    return render(request, 'index.html')
