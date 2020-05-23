from django.db import models

# Create your models here.

class Student(models.Model):
    department_name = models.ManyToManyField("department.Department",verbose_name="Department Name")
    lecture_name = models.ManyToManyField("lecture.Lecture",verbose_name="lecture_name")
    studentfullname = models.CharField(max_length = 50)
    studentbdate = models.DateTimeField(auto_now_add= False)
    def __str__(self):
       return self.studentfullname
