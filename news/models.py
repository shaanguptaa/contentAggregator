# from django.db import models


# # Create your models here.
# class Site(models.Model):
#     name = models.CharField(max_length=40)
#     short_name = models.CharField(max_length=10)
#     url = models.CharField(max_length=100)
#     rss_link = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class Article(models.Model):
#     heading = models.CharField(max_length=500)
#     summary = models.CharField(max_length=600)
#     published_date = models.CharField(max_length=15)
#     url = models.CharField(max_length=500)
#     source = models.CharField(max_length=40)

#     def __str__(self):
#         return self.heading[:100] + ' ... -  ' + self.source
