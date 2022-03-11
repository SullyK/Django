from operator import mod
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django import forms 


years_options = []
for x in range(2000, (datetime.datetime.now().year+1)):
    years_options.append(x)

def validate_legal_semester(value):
    if value >2 or value < 1:
        raise ValidationError(
            _('you entered %(value)s, please a valid semester(1 or 2)'),
            params={'value': value},
        )


class Professor(models.Model):
    name = models.CharField(max_length=34)
    initals = models.CharField(max_length=5) # change this up later

class Student(models.Model):
    student = models.CharField(max_length=34)
    password = models.CharField(max_length=34)


class Module(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)  # change this up later
    semester = models.IntegerField(validators=[validate_legal_semester])
    teachers = models.ManyToManyField(Professor)
    year = models.IntegerField(_('year'), choices=years_options, default=datetime.datetime.now().year)  

# class Rating(models.Model):
    
    
