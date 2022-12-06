from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view()),
    # path('delete/<int:pk>/', views.CarDelete.as_view()),
    # path('create/', views.CarCreate.as_view()),
    # path('update/<int:pk>/', views.CarUpdate.as_view()),
    # path('cl/', views.CarCreateList.as_view()),


]

