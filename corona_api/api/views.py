from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from . import models
from . import serializers


class VaccineListView(generics.ListAPIView):
    queryset = models.Vaccine.objects.all()
    serializer_class = serializers.VaccineSerializer
    http_method_names = ['get']

    @extend_schema(
        description='Get vaccine entities.',
        auth=None,
        tags=["Entities"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RegionListView(generics.ListAPIView):
    queryset = models.Region.objects.all()
    serializer_class = serializers.RegionSerializer
    http_method_names = ['get']

    @extend_schema(
        description='Get region entities.',
        auth=None,
        tags=["Entities"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class HospitalListView(generics.ListAPIView):
    queryset = models.Hospital.objects.all()
    serializer_class = serializers.HospitalSerializer
    http_method_names = ['get']

    @extend_schema(
        description='Get hospital entities.',
        auth=None,
        tags=["Entities"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class DistrictListView(generics.ListAPIView):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    http_method_names = ['get']

    @extend_schema(
        description='Get district entities.',
        auth=None,
        tags=["Entities"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CityListView(generics.ListAPIView):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    http_method_names = ['get']

    @extend_schema(
        description='Get city entities.',
        auth=None,
        tags=["Entities"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class AgTestsReportView(generics.ListAPIView):
    queryset = models.AgTestsReport.objects.all().order_by('id')
    serializer_class = serializers.AgTestsReportSerializer
    http_method_names = ['get']
    filter_fields = ['district_id', 'published_on']

    @extend_schema(
        description='Get ag tests reports reports.',
        auth=None,
        tags=["Reports"],
        parameters=[
            OpenApiParameter(
                name='district_id',
                type=OpenApiTypes.INT,
                description='Filter by district id.'
            ),
            OpenApiParameter(
                name='published_on',
                type=OpenApiTypes.DATE,
                description='Filter by date.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class BedsReportView(generics.ListAPIView):
    queryset = models.BedsReport.objects.all().order_by('id')
    serializer_class = serializers.BedsReportSerializer
    http_method_names = ['get']
    filter_fields = ['hospital_id', 'published_on']

    @extend_schema(
        description='Get beds reports.',
        tags=["Reports"],
        parameters=[
            OpenApiParameter(
                name='hospital_id',
                type=OpenApiTypes.INT,
                description='Filter by hospital id.'
            ),
            OpenApiParameter(
                name='published_on',
                type=OpenApiTypes.DATE,
                description='Filter by date.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class HospitalStaffReportView(generics.ListAPIView):
    queryset = models.HospitalStaffReport.objects.all().order_by('id')
    serializer_class = serializers.HospitalStaffReportSerializer
    http_method_names = ['get']
    filter_fields = ['hospital_id', 'published_on']

    @extend_schema(
        description='Get hospital staff reports.',
        tags=["Reports"],
        parameters=[
            OpenApiParameter(
                name='hospital_id',
                type=OpenApiTypes.INT,
                description='Filter by hospital id.'
            ),
            OpenApiParameter(
                name='published_on',
                type=OpenApiTypes.DATE,
                description='Filter by date.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class PatientsReportView(generics.ListAPIView):
    queryset = models.PatientsReport.objects.all().order_by('id')
    serializer_class = serializers.PatientsReportSerializer
    http_method_names = ['get']
    filter_fields = ['hospital_id', 'published_on']

    @extend_schema(
        description='Get patients reports.',
        tags=["Reports"],
        parameters=[
            OpenApiParameter(
                name='hospital_id',
                type=OpenApiTypes.INT,
                description='Filter by hospital id.'
            ),
            OpenApiParameter(
                name='published_on',
                type=OpenApiTypes.DATE,
                description='Filter by date.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class VaccinationReportView(generics.ListAPIView):
    queryset = models.VaccinationReport.objects.all().order_by('id')
    serializer_class = serializers.VaccinationReportSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['vaccine_id', 'published_on']

    @extend_schema(
        description='Get vaccination reports.',
        tags=["Reports"],
        parameters=[
            OpenApiParameter(
                name='vaccine_id',
                type=OpenApiTypes.INT,
                description='Filter by vaccine id.'
            ),
            OpenApiParameter(
                name='published_on',
                type=OpenApiTypes.DATE,
                description='Filter by date.'
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
