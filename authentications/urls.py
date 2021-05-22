from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_profile, name='login'),
    path('registration/', views.registration_profile, name='registration'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
   
    
]