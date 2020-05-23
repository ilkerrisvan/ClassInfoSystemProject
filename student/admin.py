from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["studentfullname","studentbdate"]
    list_display_links=["studentfullname","studentbdate"]
    class Meta:
        model = Student
