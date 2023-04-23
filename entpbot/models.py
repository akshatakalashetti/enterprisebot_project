from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)