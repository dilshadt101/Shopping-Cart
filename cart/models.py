from django.db import models
from django.contrib.auth.models import  User


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, unique=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            "pk": self.pk
        })

class OrderItem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total