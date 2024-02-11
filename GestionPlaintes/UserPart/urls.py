from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('probleme/', views.probleme, name="probleme"),
    path('service/', views.messagerie, name="messagerie"),
    path('suggestion/', views.suggestion, name="suggestion"),
]