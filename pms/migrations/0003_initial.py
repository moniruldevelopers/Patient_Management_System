# Generated by Django 5.0.6 on 2024-12-01 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pms', '0002_remove_doctor_department_remove_doctor_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=20)),
                ('site_logo', models.ImageField(upload_to='logo/')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=100)),
                ('site_facebook', models.URLField(max_length=100)),
                ('site_x', models.URLField(max_length=100)),
                ('site_instagram', models.URLField(max_length=100)),
                ('site_pinterest', models.URLField(max_length=100)),
            ],
        ),
    ]
