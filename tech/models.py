from django.db import models


# Create your models here.
class TechSite(models.Model):
    name = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    rss_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TechArticle(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300)
    source = models.CharField(max_length=40)

    def __str__(self):
        return self.source + ' - ' + self.title[:100]
