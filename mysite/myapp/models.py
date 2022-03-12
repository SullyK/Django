from operator import mod
from pyexpat import model
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import datetime
from django import forms 

def validate_legal_semester(value):
    if value >2 or value < 1:
        raise ValidationError(
            _('you entered %(value)s, please a valid semester(1 or 2)'),
            params={'value': value},
        )


class Professor(models.Model):
    name = models.CharField(max_length=34)
    initals = models.CharField(max_length=5) # change this up later

class Module(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)  # change this up later
    semester = models.IntegerField(validators=[validate_legal_semester])
    teachers = models.ManyToManyField(Professor)
    year = models.IntegerField()  

class Rating(models.Model):
    rating = models.IntegerField() # I should make this from 0 - 5 or 1 - 5, however the heck he wants
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Professor, on_delete=models.CASCADE)
    

# class Rating(models.Model):
    
    
