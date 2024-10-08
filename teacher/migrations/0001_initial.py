# Generated by Django 5.0.7 on 2024-07-30 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('speciality', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('JUNIOR', 'Junior'), ('MIDDLE', 'Middle'), ('SENIOR', 'Senior')], default='JUNIOR', max_length=100)),
                ('image', models.ImageField(upload_to='teachers_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
    ]
