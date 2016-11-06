#! -*- coding:utf-8 -*-
from django.db import models 
from obs.obs_lecturer.models import Lecturer  

# Create your models here.

class Course(models.Model):
    lecturer = models.ForeignKey(Lecturer)  

    code = models.CharField(max_length=15) 
    name = models.CharField(max_length=30) 
    c_type = models.CharField(max_length=15) 
    credit = models.IntegerField()  
    ects = models.IntegerField()  
    lab_hour = models.IntegerField() 
    course_hour = models.IntegerField()   

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Ders"
        verbose_name_plural="Dersler"

