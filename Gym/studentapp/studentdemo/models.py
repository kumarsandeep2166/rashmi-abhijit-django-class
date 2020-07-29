from django.db import models

# Create your models here.
BLOOD_GROUP_CHOICES  = (
    ('o+ve', 'o+ve'),
    ('o-ve', 'o-ve'),
    ('A+ve', 'A+ve'),
    ('A-ve', 'A-+ve'),
    ('B+ve', 'B+ve'),
    ('B-ve', 'B-ve'),
    ('AB+ve', 'AB+ve'),
    ('AB-ve', 'AB-ve'),
)

CASTE_CHOICES =(('Gen','GEN'),('SC','SC'),('ST','ST'),('OBC','OBC'),('Others','Others'))

GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female')
        )

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    email = models.EmailField()
    phone = models.IntegerField()
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUP_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    caste = models.CharField(max_length=10, choices=CASTE_CHOICES)

    def __str__(self):
        return self.name
