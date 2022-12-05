from .models import Car
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_view


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class UserLoginView(auth_view.LoginView):
    template_name = 'home/login.html'
    next_page = reverse_lazy('home:home')


class UserLogoutView(auth_view.LogoutView):
    next_page = reverse_lazy('home:home')


