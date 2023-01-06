from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Student(AbstractUser):
    grade = models.PositiveIntegerField()
    #renaming the groups field to avoid conflict
    groups=models.ManyToManyField(Group, related_name='student_groups', blank=True)
    user_permissions=models.ManyToManyField(Permission, related_name='student_permissions', blank=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

class Teacher(AbstractUser):
    subject = models.CharField(max_length=100)
    student = models.ManyToManyField(Student)
    #renaming the groups and user_permissionss field to avoid conflict
    groups=models.ManyToManyField(Group, related_name='teacher_groups', blank=True)
    user_permissions=models.ManyToManyField(Permission, related_name='teacher_permissions', blank=True)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

class Parent(AbstractUser):
    phone = models.CharField(max_length=15)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    #renaming the groups field to avoid conflict
    groups=models.ManyToManyField(Group, related_name='parent_groups', blank=True)
    user_permissions=models.ManyToManyField(Permission, related_name='parent_permissions', blank=True)

    class Meta:
        verbose_name = 'parents'
        verbose_name_plural = 'parents'

class AttendanceRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='students')
    date = models.DateField()
    present = models.BooleanField()
