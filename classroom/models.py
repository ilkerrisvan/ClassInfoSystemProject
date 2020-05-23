from django.db import models


# Create your models here.

class Classroom(models.Model):
    department_name = models.ManyToManyField("department.Department",verbose_name="Department Name")
    lecture_name = models.ManyToManyField("lecture.Lecture",verbose_name= "lecture name")
    classroom_name = models.CharField(max_length = 50,unique=True,verbose_name="Classroom Name")
   
    
    def __str__(self):
       return self.classroom_name

# https://www.youtube.com/watch?v=PD3YnPSHC-c&list=PL-51WBLyFTg2vW-_6XBoUpE7vpmoR3ztO&index=7



'''

# Create your models here. Wassup
class Classroom(models.Model):
    name = models.CharField(max_length=15, null=False, default="001")
    type = models.CharField(max_length=50, null=False, default="Class")
    capacity = models.IntegerField(default=0)
    exam_capacity = models.IntegerField(default=0)
    sync_token = models.CharField(max_length=256, null=True, default=None)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    by = models.ForeignKey(get_user_model(), null=False, default=1, on_delete=models.SET_DEFAULT)
    res_class = models.ManyToManyField(Classroom)
    description = models.TextField(max_length=350, default="")
    student_total = models.IntegerField(default=0)
    instructor = models.CharField(max_length=1024,null=True)
    proctor_count = models.IntegerField(null=True)
    res_date_start = models.DateTimeField(null=True)
    res_date_end = models.DateTimeField(null=True)
    id_list = ArrayField(models.CharField(max_length=256, null=True, default=None), null=True, default=None)

'''