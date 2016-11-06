#! -*- coding:utf-8 -*-
from django.db import models
from obs.obs_faculty.models import Faculty

# Create your models here.

class Department(models.Model):
    faculty = models.ForeignKey(Faculty)  
    department_name = models.CharField(max_length=30)
    department_code = models.CharField(max_length=10)
    department_tel = models.CharField(max_length=20)
    department_fax = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

    class Meta:
        verbose_name ="Bölüm"
        verbose_name_plural="Bölümler"

