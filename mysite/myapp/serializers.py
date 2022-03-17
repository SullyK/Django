from attr import field
from rest_framework import serializers
from . models import Professor, Module

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id'] # sort this out later... need maybe an all and this custom one.

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'
        depth = 1