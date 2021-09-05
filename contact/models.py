from django.core import validators
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Budget(models.Model):
    min = models.PositiveIntegerField()
    max = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f'${self.min}-{self.max}'


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Project(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    budget = models.ForeignKey('Budget', on_delete=models.CASCADE)
    description = models.TextField()

    


