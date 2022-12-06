from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('<int:pk>/', views.Home.as_view()),

]

