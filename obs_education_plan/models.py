#! -*- coding:utf-8 -*-
from django.db import models 
from obs.obs_department.models import Department
from obs.obs_semester.models import Semester 

# Create your models here.

class EducationPlan(models.Model):
    department = models.ForeignKey(Department)
    semester = models.ForeignKey(Semester)  
    accept_date = models.CharField(max_length=15) 

    def __str__(self):
        return self.department.department_name+" "+self.semester.name

    class Meta:
        verbose_name ="Eğitim Planı"
        verbose_name_plural="Eğitim Planları"

