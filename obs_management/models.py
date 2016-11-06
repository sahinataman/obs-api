#! -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from obs.obs_department.models import Department

# Create your models here.

class Management(models.Model):
    user = models.OneToOneField(User)
    degree = models.CharField(max_length=15)
    m_type = models.CharField(max_length=15) 
    phone = models.CharField(max_length=12,blank=True, null=True)
    fax = models.CharField(max_length=12,blank=True, null=True) 
    address = models.CharField(max_length=15) 
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES) 
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name

    class Meta:
        verbose_name ="Yönetim Üyesi"
        verbose_name_plural="Yönetim Üyeleri"

