from django.contrib import admin
from .models import TA

@admin.register(TA)
class TAAdmin(admin.ModelAdmin):

    class Meta:
        model = TA