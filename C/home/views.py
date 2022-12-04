from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.views.generic.list import ListView
from .models import Car


# class Home(TemplateView):
    # http_method_names = ['get', 'post', 'options']
    #
    # def get(self, request):
    #     return render(request, 'home/home.html')
    #
    # def options(self, request, *args, **kwargs):
    #     response = super().options(request, *args, **kwargs)
    #     response.headers['host'] = 'localhost'
    #     response.headers['user'] = request.user
    #     return response
    #
    # def http_method_not_allowed(self, request, *args, **kwargs):
    #     return render(request, 'method_not_allowed.html')



    # template_name = 'home/home.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['cars'] = Car.objects.all()
    #     return context


class Home(ListView):
    template_name = 'home/home.html'
    # model = Car
    # queryset = Car.objects.filter(year__gte=2000)
    context_object_name = 'cars'
    # ordering = 'year'

    def get_queryset(self):
        return Car.objects.filter(year__gte=2000)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = 'jack'
        return context

# class Two(RedirectView):
#
#     # url = 'https://google.com'
#     # pattern_name = 'home:home'
#     #
#     # def get_redirect_url(self, *args, **kwargs):
#     #     print('='*90)
#     #     print(kwargs['id'], kwargs['name'])
#     #     return super().get_redirect_url(*args, **kwargs)
#
#     url = '/home/%(id)s/%(name)s/'
#
#     def get_redirect_url(self, *args, **kwargs):
#         print('='*90)
#         return super().get_redirect_url(*args, **kwargs)
