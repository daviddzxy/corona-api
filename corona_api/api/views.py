from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from . import serializers


class VaccineListView(generics.ListAPIView):
    queryset = models.Vaccine.objects.all()
    serializer_class = serializers.VaccineSerializer
    http_method_names = ['get']


class RegionListView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    http_method_names = ['get']


class HospitalListView(generics.ListAPIView):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    http_method_names = ['get']


class DistrictListView(generics.ListAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    http_method_names = ['get']


class CityListView(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    http_method_names = ['get']


class AgTestsReportView(generics.ListAPIView):
    queryset = models.AgTestsReport.objects.all().order_by('id')
    serializer_class = serializers.AgTestsReportSerializer
    http_method_names = ['get']
    filter_fields = ['district_id', 'published_on']


class BedsReportView(generics.ListAPIView):
    queryset = models.BedsReport.objects.all().order_by('id')
    serializer_class = serializers.BedsReportSerializer
    http_method_names = ['get']
    fitler_fields = ['hospital_id', 'published_on']


class HospitalStaffReportView(generics.ListAPIView):
    queryset = models.HospitalStaffReport.objects.all().order_by('id')
    serializer_class = serializers.HospitalStaffReportSerializer
    http_method_names = ['get']
    filter_fields = ['hospital_id', 'published_on']


class PatientsReportView(generics.ListAPIView):
    queryset = models.PatientsReport.objects.all().order_by('id')
    serializer_class = serializers.PatientsReportSerializer
    http_method_names = ['get']
    filter_fields = ['hospital_id', 'published_on']


class VaccinationReportView(generics.ListAPIView):
    queryset = models.VaccinationReport.objects.all().order_by('id')
    serializer_class = serializers.VaccinationReportSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['vaccine_id', 'published_on']
