from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="page_1"),
    path('logout/', views.logout_view, name="logout"),
]