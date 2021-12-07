from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title


class OrderItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

