from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db import IntegrityError


def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = get_user_model()
        try:
            existing_user = User.objects.get(email=email)
            return render(request, 'existing_user_error.html')
        except User.DoesNotExist:
            user = User.objects.create_user(email=email, password=password)
            return render(request, 'user_created_successfully.html')

    return render(request, 'index.html')
