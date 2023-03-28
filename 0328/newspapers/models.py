from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    journalist = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)