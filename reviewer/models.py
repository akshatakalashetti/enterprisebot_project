from django.db import models

# Create your models here.
class Reviews(models.Model):
    title = models.TextField()
    review_body = models.TextField()
    size = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    is_verified_purchase = models.BooleanField(default=False)
    sentiment = models.TextField(default='neutral', blank=True)
    polarity_score = models.FloatField(default=0.0)