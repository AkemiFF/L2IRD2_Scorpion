from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('probleme/', views.probleme, name="probleme"),
    path('messagerie/', views.messagerie, name="messagerie"),
    path('suggestion/', views.suggestion, name="suggestion"),
    path('delete_message/<int:mess_id>', views.delete_message, name="delete_message"),

]