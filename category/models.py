from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.title