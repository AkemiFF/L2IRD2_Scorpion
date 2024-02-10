from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('probleme/', views.probleme, name="probleme"),
    path('suggestion/', views.suggestion, name="suggestion"),
]