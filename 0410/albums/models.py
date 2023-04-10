from django.db import models


class Album(models.Model):
    content = models.CharField(max_length=20)
    image = models.ImageField(blank=True)