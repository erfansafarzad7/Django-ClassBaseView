from .models import Car
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView, ListCreateAPIView
from .serializers import CarSerializer


class Home(ListAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()


# class CarDelete(DestroyAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()


# class CarCreate(CreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()


# class CarUpdate(UpdateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()


# class CarCreateList(ListCreateAPIView):
#     serializer_class = CarSerializer
#     queryset = Car.objects.all()




