from django.db import models

# Create your models here.
SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

class College(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Student(models.Model):
    name =  models.CharField(max_length=200)
    roll_number = models.IntegerField()
    email = models.EmailField(max_length=50)
    age = models.IntegerField()
    # dob = models.DateField
    address = models.TextField(max_length=250)
    size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='S')
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


