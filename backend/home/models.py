from django.db import models


class Home(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    logo = models.ImageField(upload_to='home_images/', verbose_name="Logo")

    class Meta:
        verbose_name = "Home"
        verbose_name_plural = "Homes"

    def __str__(self):
        return self.title