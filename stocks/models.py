from django.db import models


# Create your models here.
class TopGainer(models.Model):
    company = models.CharField(max_length=30)
    high = models.FloatField()
    low = models.FloatField()
    last = models.FloatField()
    prev = models.FloatField()

    def __str__(self):
        return self.company


class TopLoser(models.Model):
    company = models.CharField(max_length=30)
    high = models.FloatField()
    low = models.FloatField()
    last = models.FloatField()
    prev = models.FloatField()

    def __str__(self):
        return self.company
