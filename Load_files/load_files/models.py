from django.db import models


class File(models.Model):
    file = models.FileField(blank=True, null=True, upload_to='files/', verbose_name='файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='дата и время загрузки', null=True, blank=True)
    processed = models.BooleanField(default=False, verbose_name='статус выполнения')

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return str(self.processed)

