from django.contrib import admin
from load_files.models import *


class FileAdmin(admin.ModelAdmin):
    list_display = ['file', 'uploaded_at', 'processed']


admin.site.register(File, FileAdmin)

