from django.db import models

# Create your models here.
class BMIRecord(models.Model):
    weight = models.FloatField()
    height = models.FloatField()
    # bmi = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)