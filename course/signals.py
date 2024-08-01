from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import json
from course.models import Course
from root.settings import BASE_DIR
import os


@receiver(pre_delete, sender=Course)
def save_deleted_course(sender, instance, **kwargs):
    file_name = os.path.join(BASE_DIR, 'course/deleted_courses', f'course_{instance.id}.json')
    print(f'{instance.title} has been deleted')
    data = {
        'id': instance.id,
        'title': instance.title,
        'description': instance.description,
        'price': instance.price,
        'number_of_students': instance.number_of_students,
        'duration': instance.duration,
        }

    with open(str(file_name), 'a') as file:
        json.dump(data, file, indent=4)

