from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    others = models.TextField(blank=True)
    
    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
