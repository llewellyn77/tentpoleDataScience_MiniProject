from django.db import models
from datetime import datetime,date 


# Create your models here.
#migrated to postgresql db
class CustomerInformation(models.Model):
    fName =models.CharField(max_length=200)
    lName =models.CharField(max_length=200)
    dateOfBirth =models.DateField( blank=True, null=True)
    excelFile = models.FileField()