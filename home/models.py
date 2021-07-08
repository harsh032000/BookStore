from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100, null=True)
    genre = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name