from .models import Car
from django.views.generic import ListView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class CarCreateView(CreateView):
    model = Car
    fields = ['name', 'year']
    template_name = 'home/create.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = self.request.user.username if self.request.user.username else 'None'
        form.save()
        messages.success(self.request, 'successfully created', 'success')
        return super().form_valid(form)

