from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=10)

    def __str__(self):
        return self.name