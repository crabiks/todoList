from django.db import models
from colorfield.fields import ColorField

class Category(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=120
    )
    color = ColorField(default="#FF0000")


class Task(models.Model):
    category = models.ForeignKey(
        Category,
        verbose_name="Category",
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=120
    )
    description = models.TextField(
        verbose_name="Description"
    )