# Generated by Django 3.2.4 on 2021-06-30 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210630_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]