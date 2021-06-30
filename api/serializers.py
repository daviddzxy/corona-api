from rest_framework import serializers
from .models import Vaccine, Region, VaccinationReport, District, AgTestsReport, City, Hospital, HospitalStaffReport,\
    BedsReport, PatientsReport


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'


class AgTestsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgTestsReport
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class HospitalStaffReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalStaffReport
        fields = '__all__'


class BedsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedsReport
        fields = '__all__'


class PatientsReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsReport
        fields = '__all__'

class VaccinationReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationReport
        fields = '__all__'