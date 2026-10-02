from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField(blank=True)

    image = models.ImageField(
        upload_to="food/",
        blank=True,
        null=True
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="foods"
    )

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.date}"