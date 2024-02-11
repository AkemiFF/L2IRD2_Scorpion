from django.urls import path
from . import views

urlpatterns = [
    path('', views.back, name="backoffice"),
    path('info/<int:problem_id>/', views.ViewInfo, name="viewinfo"),
    path('feedback/<int:problem_id>/', views.feedback, name='feedback'),
    path('cloturer/<int:problem_id>/', views.cloturer, name='cloturer'),
]