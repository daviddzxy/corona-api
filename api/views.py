from rest_framework import generics
from .serializers import VaccineSerializer
from .models import Vaccine


class VaccineList(generics.ListAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    http_method_names = ['get']
