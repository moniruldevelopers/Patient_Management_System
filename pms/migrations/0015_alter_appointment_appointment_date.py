# Generated by Django 5.0.6 on 2025-02-14 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0014_alter_appointment_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(),
        ),
    ]
