import os
from celery import Celery
import logging
from celery.utils.log import get_task_logger

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Load_files.settings')

app = Celery('Load_files')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


def logger_settings():
    logger = get_task_logger('celery_logging')
    logger.setLevel(logging.INFO)
    handler_c = logging.FileHandler("celery_logging_file.log", mode='a')
    formatter_c = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
    handler_c.setFormatter(formatter_c)
    logger.addHandler(handler_c)
    return logger
