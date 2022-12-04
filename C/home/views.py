from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Car


class Home(ListView):
    template_name = 'home/home.html'
    model = Car
    context_object_name = 'cars'


class CarDetail(DetailView):
    template_name = 'home/detail.html'
    # model = Car
    # context_object_name = 'car'
    # slug_field = 'name'
    # slug_url_kwarg = 'my_slug'
    # pk_url_kwarg = 'my_pk'
    # queryset = Car.objects.filter(year__gte=2000)

    # def get_queryset(self):
    #     if self.request.user.is_authenticated:
    #         return Car.objects.filter(name=self.kwargs['pk'])
    #     else:
    #         return Car.objrcts.none()

    def get_object(self, queryset=None):
        return Car.objects.get(
            name=self.kwargs['name'],
            year=self.kwargs['year'],
            owner=self.kwargs['owner'],
        )



