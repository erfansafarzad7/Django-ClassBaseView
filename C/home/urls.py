from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<int:year>/<int:month>/', views.MonthCarView.as_view()),

]

