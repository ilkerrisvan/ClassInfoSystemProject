from django.db import models

# Create your models here.
# Create your models here.
class TA(models.Model):
        ta_name = models.CharField(max_length = 50,unique=True,verbose_name="Instructor Name ")
        ta_bdate = models.DateTimeField(auto_now_add= False,verbose_name="Instructor Birthday ")
        image_events = models.ImageField(upload_to='image',blank=True,verbose_name="Picture of Instructor ")
    
     
        def __str__(self):
          return self.ta_name