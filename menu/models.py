from django.db import models


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="Category")
    icon_image = models.ImageField()


class Food(models.Model):
    title = models.CharField(max_length=50, verbose_name="Food")
    description = models.TextField(max_length=500, verbose_name="Description")
    price = models.IntegerField(verbose_name="Price")
    icon_image = models.ImageField()
    date_create = models.DateTimeField(auto_created=True)



