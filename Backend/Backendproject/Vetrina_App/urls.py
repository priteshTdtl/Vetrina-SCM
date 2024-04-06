from django.urls import path
from . import signup, login


urlpatterns = [
    path('Signup_view/', signup.Signup_view, name='Vetrina_App'),
    path('Login_view/',login.Login_view,name="Login_view"),
]