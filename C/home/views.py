from .models import Car
from django.views.generic import ListView, MonthArchiveView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_view


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class MonthCarView(MonthArchiveView):
    model = Car
    date_field = 'created'
    template_name = 'home/home.html'
    context_object_name = 'cars'
    month_format = '%m'

