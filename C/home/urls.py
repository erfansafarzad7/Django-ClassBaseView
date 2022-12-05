from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('create/', views.CarCreateView.as_view(), name='create'),

]

