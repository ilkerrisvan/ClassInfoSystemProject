from django.db import models

# Create your models here.
class Lecture(models.Model):
        l_name = models.CharField(max_length = 50,unique=True,verbose_name="Course Name")
        l_date = models.DateTimeField(auto_now_add= False,verbose_name="Course Start Date")
        l_date_end = models.DateTimeField(auto_now_add= False,verbose_name="Course Finish Date")
        ta_name = models.ManyToManyField("ta.TA",verbose_name="Instructor Name")
        
        def __str__(self):
          return self.l_name
