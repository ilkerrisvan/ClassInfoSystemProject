from django.db import models

# Create your models here.


class Department(models.Model):
    d_name = models.CharField(max_length = 50,unique=True,verbose_name="Department Name")
    def  __str__(self):
       return self.d_name
       