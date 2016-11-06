#! -*- coding:utf-8 -*-
from django.db import models 
from obs.obs_student.models import Student
from obs.obs_offered_course.models import OfferedCourse  

# Create your models here.

class Register(models.Model):
    student = models.ForeignKey(Student)  
    offered_course = models.ForeignKey(OfferedCourse)  
 

    def __str__(self):
        return self.student.user.first_name+"  "+self.student.user.last_name+" Öğrencisi  "+self.offered_course.course.name+" Dersi"

    class Meta:
        verbose_name ="Öğrenci Tarafından Seçilen Ders"
        verbose_name_plural="Öğrenci Tarafından Seçilen Dersler"

