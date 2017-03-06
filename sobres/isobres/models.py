from django.db import models

# Create your models here.
class Sobre(models.Model):
    amount = models.IntegerField()
    concept = models.TextField(max_length=100)
    date = models.DateTimeField()
