from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
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
    queryset = models.AgTestsReport.objects.all()
    serializer_class = serializers.AgTestsReportSerializer
    http_method_names = ['get']


class BedsReportView(generics.ListAPIView):
    queryset = models.BedsReport.objects.all()
    serializer_class = serializers.BedsReportSerializer
    http_method_names = ['get']


class HospitalStaffReportView(generics.ListAPIView):
    queryset = models.HospitalStaffReport.objects.all()
    serializer_class = serializers.HospitalStaffReportSerializer
    http_method_names = ['get']


class PatientsReportView(generics.ListAPIView):
    queryset = models.PatientsReport.objects.all()
    serializer_class = serializers.PatientsReportSerializer
    http_method_names = ['get']


class VaccinationReportView(generics.ListAPIView):
    queryset = models.VaccinationReport.objects.all()
    serializer_class = serializers.VaccineSerializer
    http_method_names = ['get']


class VaccineVaccinationReport(APIView):
    def get(self, request, pk):
        vaccination_reports = models.VaccinationReport.objects.filter(vaccine_id=pk)
        serializer = serializers.VaccinationReportSerializer(vaccination_reports, many=True)
        return Response(serializer.data)

