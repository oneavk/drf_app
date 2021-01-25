from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
        ordering = ('id',)

    def __str__(self):
        return f'{self.id}: {self.name}'
