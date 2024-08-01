from django.db.models.signals import pre_delete
from django.dispatch import receiver
import json
from teacher.models import *
from root.settings import BASE_DIR
import os


@receiver(pre_delete, sender=Teacher)
def save_deleted_course(sender, instance, **kwargs):
    file_name = os.path.join(BASE_DIR, 'teacher/deleted_teachers', f'teacher_{instance.id}.json')
    print(f'{instance.full_name} has been deleted')
    data = {
        'id': instance.id,
        'full_name': instance.full_name,
        'email': instance.email,
        'speciality': instance.speciality,
        'level': instance.level,
        }

    with open(str(file_name), 'a') as file:
        json.dump(data, file, indent=4)
