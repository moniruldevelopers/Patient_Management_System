# Generated by Django 5.0.6 on 2024-12-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0006_patientprofile_patient_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientIDTracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_patient_id', models.BigIntegerField(default=1000000000)),
            ],
        ),
    ]
