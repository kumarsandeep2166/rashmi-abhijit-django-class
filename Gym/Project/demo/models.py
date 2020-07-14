from django.db import models

# Create your models here.
class Student(models.Model):
    name =  models.CharField(max_length=200)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    # dob = models.DateField
    address = models.TextField(max_length=250)

    def __str__(self):
        return self.name


