#! -*- coding:utf-8 -*-
from django.db import models 
from obs.obs_course.models import Course
from obs.obs_semester.models import Semester  

# Create your models here.

class OfferedCourse(models.Model):
    course = models.ForeignKey(Course)  
    semester = models.ForeignKey(Semester)  
 

    def __str__(self):
        return self.semester.name+" Dönemi "+self.course.name+" Dersi"

    class Meta:
        verbose_name ="Açılan Ders"
        verbose_name_plural="Açılan Dersler"

