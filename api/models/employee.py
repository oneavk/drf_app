from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='employees')

    class Meta:
        ordering = ('last_name', 'first_name', 'middle_name')

    def __str__(self):
        return f'{self.id}: {self.name}'
