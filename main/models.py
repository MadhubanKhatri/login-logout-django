from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=15)

    def __str__(self):
        return self.fname
        
