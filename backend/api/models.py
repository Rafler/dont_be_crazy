from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Event(models.Model):
    is_active = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField()
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.name