from .models import Car
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, DestroyModelMixin
from rest_framework.response import Response
from .serializers import CarSerializer


class Home(RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    serializer_class = CarSerializer
    queryset = Car.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.name == 'BENZ':
            return Response('Sorry..')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

