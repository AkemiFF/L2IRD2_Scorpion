from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="page_1"),
    path('admin_login/', views.adminlogin, name="adminLogin"),
    path('logout/', views.logout_view, name="logout"),
    path('password_lost/', views.password_lost, name="password_lost"),

]