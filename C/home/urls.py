from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    # path('<slug:my_slug>/', views.CarDetail.as_view(), name='car_detail'),
    path('<str:name>/<int:year>/<str:owner>/', views.CarDetail.as_view(), name='car_detail'),
]

