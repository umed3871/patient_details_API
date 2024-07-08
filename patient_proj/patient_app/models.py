from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.BigIntegerField(default=1)
    dob = models.DateField()