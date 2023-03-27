from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email
