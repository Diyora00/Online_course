# Generated by Django 5.0.7 on 2024-07-30 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='subjects',
            new_name='subject',
        ),
    ]
