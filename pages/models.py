from email import message
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contact(models.Model):
    firs_name = models.CharField( max_length=100)
    last_name = models.CharField( max_length=100)
    email = models.EmailField( max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(max_length=11,blank=True)
    
    
    def __str__(self):
        return self.email