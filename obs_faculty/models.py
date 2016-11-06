#! -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=50)
    faculty_code = models.CharField(max_length=20)  
    faculty_address = models.CharField(max_length=220) 
    faculty_tel = models.CharField(max_length=12) 
    faculty_fax = models.CharField(max_length=12) 

    def __str__(self):
        return self.faculty_name

    class Meta:
        verbose_name ="Fakülte"
        verbose_name_plural="Fakülteler"

