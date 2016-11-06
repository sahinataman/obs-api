#! -*- coding:utf-8 -*-
from django.db import models 

# Create your models here.

class Semester(models.Model):
    
    name = models.CharField(max_length=15)  
    elective_credits = models.IntegerField() 
    compulsory_credits = models.IntegerField() 
    course_amount = models.IntegerField() 
    total_elective_amount = models.IntegerField()  

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Dönem"
        verbose_name_plural="Dönemler"

