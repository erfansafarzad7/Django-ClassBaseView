from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', views.UserLoginView.as_view(), name='login'),


]

