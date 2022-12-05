from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('delete/<int:pk>', views.CarDeleteView.as_view(), name='car_delete'),


]

