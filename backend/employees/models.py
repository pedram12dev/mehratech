from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='employees/images/')

    def __str__(self):
        return self.full_name
    