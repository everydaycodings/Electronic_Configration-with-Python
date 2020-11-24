from django.db import models

# Create your models here.

class ContactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    message= models.TextField()

    def __str__(self):
        return self.name
