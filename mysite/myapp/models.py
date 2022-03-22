from operator import mod
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
    initals = models.CharField(max_length=8) # change this up later
    def __str__(self) -> str:
        return str(self.name + ' ' + self.initals )

class Module(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=5)  # change this up later
    semester = models.IntegerField(validators=[validate_legal_semester])
    teachers = models.ManyToManyField(Professor)
    year = models.IntegerField()  
    def __str__(self) -> str:
        empty = ""
        for x in self.teachers.all():
            empty += x.name + ',' + x.initals + ' '

        
        return str(self.name  + ',' + self.code + ' ' +  'semester ' + str(self.semester) + ' ' + str(self.year) + ' ' + empty )
        empty = ""


class Rating(models.Model):
    rating = models.IntegerField() # I should make this from 0 - 5 or 1 - 5, however the heck he wants
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    teachers = models.ForeignKey(Professor, on_delete=models.CASCADE)
    def __str__(self) -> str:
        mod_name = ""
        mod_teacher = ""
        

        return str("Rated " + ' ' + str(self.rating) + ',' + self.teachers.name + ' ' +  self.module.name + ' ' + self.module.code + ' ' + 'Semester ' +  str(self.module.semester) + ' Year ' +  ' ' + str(self.module.year)) 