from django.db import models
from django.conf import settings


# Create your models here.
class Nota(models.Model):

    title = models.CharField(
      'titulo', 
      max_length=30
    )
    description = models.TextField('descripcion')
    user_created = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE,
    )

    class Meta:
      verbose_name = 'Nota'
      verbose_name_plural = 'Notas'

    def __str__(self):
        return self.title
