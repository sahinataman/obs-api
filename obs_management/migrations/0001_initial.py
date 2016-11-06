# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-06 10:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('obs_department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=15)),
                ('m_type', models.CharField(max_length=15)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('fax', models.CharField(blank=True, max_length=12, null=True)),
                ('address', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obs_department.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Yönetim Üyeleri',
                'verbose_name': 'Yönetim Üyesi',
            },
        ),
    ]