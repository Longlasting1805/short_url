from django.db import models


# Create your models here.

class Shrink(models.Model):
    url_link = models.CharField(max_length=200)
    slug = models.CharField(max_length=15)

    def __str__(self):
        return self.url_link
