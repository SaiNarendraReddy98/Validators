from django.db import models

# Create your models here.
class Student(models.Model):
    Sname = models.CharField(max_length=100)
    Snumber = models.IntegerField()
    Slocation = models.CharField(max_length=100)
    email = models.EmailField(default='welcome@gmail.com')
    renteremail = models.EmailField(default='welcome@gmail.com')
    def __str__(self):
        return self.Sname
    