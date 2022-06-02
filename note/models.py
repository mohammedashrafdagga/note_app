from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.category_name)


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
