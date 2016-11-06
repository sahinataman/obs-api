#! -*- coding:utf-8 -*-
from django.db import models 
from obs.obs_register.models import Register 

# Create your models here.

class RegisterNote(models.Model):
    register = models.OneToOneField(Register)
    mid_exam = models.IntegerField()
    final_exam = models.IntegerField()
    make_up_exam = models.IntegerField(null=True) 
    make_up_exam_status = models.BooleanField(default=False)
     
 
    def __str__(self):
        return self.register.student.user.first_name+"  "+self.register.student.user.last_name+" Öğrencisi  "+self.register.offered_course.course.name+" Dersi"

    class Meta:
        verbose_name ="Seçilen Dersin Notu"
        verbose_name_plural="Seçilen Derslerin Notlari"

