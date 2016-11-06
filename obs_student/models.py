#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from obs.obs_department.models import Department

# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    number = models.CharField(max_length=15)
    active_record_semester = models.CharField(max_length=50)
    birthdate = models.CharField(max_length=20)
    phone = models.CharField(max_length=12,blank=True, null=True)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

    class Meta:
        verbose_name ="Öğrenci"
        verbose_name_plural="Öğrenciler"

