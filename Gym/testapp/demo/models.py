from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=64)
    roll = models.IntegerField()
    marks = models.FloatField()
    addr = models.TextField()

    def __str__(self):
        return self.name