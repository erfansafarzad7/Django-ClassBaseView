from .models import Car
from .forms import CarCreateForm
from django.views.generic import ListView, FormView
from django.urls import reverse_lazy
from django.contrib import messages


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class CarCreateView(FormView):
    template_name = 'home/create.html'
    form_class = CarCreateForm
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        self._car_create(form.cleaned_data)
        messages.success(self.request, 'car successfully created', 'success')
        return super().form_valid(form)

    def _car_create(self, data):
        Car.objects.create(name=data['name'], owner=data['owner'], year=data['year'])

