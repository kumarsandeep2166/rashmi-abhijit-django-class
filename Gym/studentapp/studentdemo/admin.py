from django.contrib import admin
from .models import Student
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'created_at', 'email', 'phone']


admin.site.register(Student, StudentAdmin)