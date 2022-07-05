from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name = 'dashboard-register'),
    path('profile/', views.profile, name = 'dashboard-profile'),
    
]