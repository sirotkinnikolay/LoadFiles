from celery import Celery
from decouple import config
from load_files.models import *
from load_files.serializers import *
from django.core.files.base import ContentFile

app = Celery('myapp', broker=f'{config("REDIS_HOST")}://{config("REDIS_HOST")}:{config("REDIS_PORT")}/0')


@app.task
def load_file_and_changing_status(file_content, file_name):
    file_instance = File()
    file_instance.file.save(file_name, ContentFile(file_content))
    file_instance.save()
    file_instance.processed = True
    file_instance.save()


