from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('acceuil/', include('UserPart.urls')),
    path('population/', include('UserPart.urls')),
]
