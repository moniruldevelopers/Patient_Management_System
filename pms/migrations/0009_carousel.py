# Generated by Django 5.0.6 on 2025-02-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pms', '0008_siteinfo_opening_hours'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
