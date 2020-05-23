from django.db import models

# Create your models here.

class Ads(models.Model):
    ads_name = models.CharField(max_length = 50,unique=True,verbose_name="Ads Name")
    dep_name =models.ManyToManyField("department.Department",verbose_name="Department Name")
    image_ads = models.ImageField(upload_to='image',blank=True,verbose_name="Image of Ads")
    def __str__(self):
       return self.ads_name
