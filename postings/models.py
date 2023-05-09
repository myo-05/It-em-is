from django.db import models
from users.models import User
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    likes = models.ManyToManyField(User, related_name="like_articles")

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('detail_view', kwargs={'article_id': self.id})