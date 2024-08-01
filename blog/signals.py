from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
import json
from blog.models import Blog
from root.settings import BASE_DIR
import os


@receiver(pre_delete, sender=Blog)
def save_deleted_course(sender, instance, **kwargs):
    file_name = os.path.join(BASE_DIR, 'blog/deleted_blogs', f'blog_{instance.id}.json')
    print(f'{instance.title} has been deleted')
    data = {
        'id': instance.id,
        'title': instance.title,
        'body': instance.body,
        }

    with open(str(file_name), 'a') as file:
        json.dump(data, file, indent=4)
