from django.db import models

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length = 50,unique=True,verbose_name="Event Name")
    dept_name =models.ManyToManyField("department.Department",verbose_name="Department Name")
    image_events = models.ImageField(upload_to='image',blank=True,verbose_name="Picture of Event")
    def __str__(self):
       return self.event_name
