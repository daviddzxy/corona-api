from django.db import models


class Region(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=5)
    abbreviation = models.CharField(max_length=2)


class Vaccine(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150)


class VaccinationReport(models.Model):
    id = models.CharField(primary_key=True, max_length=18)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    dose1_count = models.PositiveIntegerField(null=True)
    dose2_count = models.PositiveIntegerField(null=True)
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class District(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=6)


class City(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    code = models.CharField(max_length=12)


class Hospital(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=16)


class HospitalStaffReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    out_of_work_ratio_doctor = models.FloatField(null=True)
    out_of_work_ratio_nurse = models.FloatField(null=True)
    out_of_work_ratio_other = models.FloatField(null=True)
    reported_at = models.DateTimeField
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class PatientsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    ventilated_covid = models.PositiveIntegerField(null=True)
    non_covid = models.PositiveIntegerField(null=True)
    confirmed_covid = models.PositiveIntegerField(null=True)
    suspected_covid = models.PositiveIntegerField(null=True)
    reported_at = models.DateTimeField
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class BedsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    capacity_all = models.PositiveIntegerField(null=True)
    free_all = models.PositiveIntegerField(null=True)
    capacity_covid = models.PositiveIntegerField(null=True)
    occupied_jis_covid = models.PositiveIntegerField(null=True)
    occupied_oaim_covid = models.PositiveIntegerField(null=True)
    occupied_o2_covid = models.PositiveIntegerField(null=True)
    occupied_other_covid = models.PositiveIntegerField(null=True)
    reported_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    published_on = models.DateField()


class AgTestsReport(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    positivity_rate = models.FloatField(null=True)
    positives_count = models.PositiveIntegerField(null=True)
    negatives_count = models.PositiveIntegerField(null=True)
    positives_sum = models.PositiveIntegerField(null=True)
    negatives_sum = models.PositiveIntegerField(null=True)
    updated_at = models.DateTimeField()
    published_on = models.DateField()
