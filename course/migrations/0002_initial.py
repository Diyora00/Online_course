# Generated by Django 5.0.7 on 2024-07-30 13:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teachers',
            field=models.ManyToManyField(related_name='courses', to='teacher.teacher'),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.course'),
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='course.subject'),
        ),
    ]