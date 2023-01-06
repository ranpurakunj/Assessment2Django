from django.contrib import admin
from .models import Student, Teacher, Parent, AttendanceRecord
# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(AttendanceRecord)