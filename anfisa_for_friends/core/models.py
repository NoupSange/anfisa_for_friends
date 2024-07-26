from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаг is_published."""
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    class Meta:
        abstract = True
