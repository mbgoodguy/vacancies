from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=60)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    address = models.CharField(max_length=60)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=50)
