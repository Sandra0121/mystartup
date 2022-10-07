from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(blank=False, null=False, default=False)

def get_absolute_url(self):
    return reverse("products:detail", kwargs={"my_id": self.my_id})