from django.urls import path, include
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    # path('two/<int:id>/<str:name>', views.Two.as_view(), name='two'),
]