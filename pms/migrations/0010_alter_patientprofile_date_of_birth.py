# Generated by Django 5.0.6 on 2024-12-27 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0009_doctorprofile_image_alter_doctorprofile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientprofile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
