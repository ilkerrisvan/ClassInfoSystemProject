from django.contrib import admin
from .models import Classroom


admin.site.site_header = "Class Info - Admin Panel"


# Register your models here.
@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Classroom
     
