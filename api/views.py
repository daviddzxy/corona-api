from rest_framework import generics
from .serializers import VaccineSerializer, RegionSerializer, HospitalSerializer, DistrictSerializer, CitySerializer
from .models import Vaccine, Region, Hospital, District, City


class VaccineListView(generics.ListAPIView):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    http_method_names = ['get']


class RegionListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    http_method_names = ['get']


class HospitalListView(generics.ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer


class DistrictListView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer