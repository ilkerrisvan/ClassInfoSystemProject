from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from lecture.models import *
from department.models import *
from ads.models import *
from events.models import *
from student.models import *
from datetime import datetime
from django.utils import timezone
from ta.models import *
import pytz



def classpick(request):
    classes = Classroom.objects.all()
    
    context = {
        'class':classes,
        
    }
    return render(request, 'index.html',context)

def about(request,pk_test):
    classes = Classroom.objects.get(classroom_name=pk_test)
    department = Department.objects.all()
    ads= Ads.objects.all()
    events= Events.objects.all()
    student=Student.objects.all()
    lectures = Lecture.objects.all()
    mydate = datetime.today()
    print(classes)
    print(department)
    print("ADS ADS ADS ",ads)
    print(student)
    print("Lecture Objects: ",lectures)
    print("student",student)
    print(mydate)
    context = {'classes':classes,'department':department,'ads':ads,'student':student,'lecture':lectures,'mydate':mydate,'events':events}
    return render(request,'about.html',context)

def schedule(request,pk_test):
    student=Student.objects.all()
    lectures = Lecture.objects.all()
    mydate = datetime.today()
    classes = Classroom.objects.get(classroom_name=pk_test)
    department = Department.objects.all()
    ads= Ads.objects.all()
    print("Lecture Objects: ",lectures)
    print("student",student)
    print(mydate)
    context = {'classes':classes,'department':department,'ads':ads,'student':student,'lecture':lectures,'mydate':mydate}
    return render(request,'schedule.html',context)
    
def information(request,pk_test):
    ta = TA.objects.all()
    classes = Classroom.objects.get(classroom_name=pk_test)
    department = Department.objects.all()
    ads= Ads.objects.all()
    events= Events.objects.all()
    student=Student.objects.all()
    lectures = Lecture.objects.all()
    mydate = datetime.today()
   
    print("Classrooms",classes)
    print(department)
    print("ADS ADS ADS ",ads)
    print(student)
    print("Lecture Objects: ",lectures)
    print("student",student)
    print(mydate)
    print("*************",ta)
    print("*************",department)
    context = {'classes':classes,'department':department,'ads':ads,'student':student,'lecture':lectures,'mydate':mydate,'events':events,'ta':ta}
    return render(request,'information.html',context)




