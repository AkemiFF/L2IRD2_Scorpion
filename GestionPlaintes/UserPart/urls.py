from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('probleme/', views.probleme, name="probleme"),
    path('messagerie/', views.messagerie, name="messagerie"),
    path('suggestion/', views.suggestion, name="suggestion"),
]