from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Professor, Module
from . serializers import ProfessorSerializer, ModuleSerializer


@api_view(["GET"])
def index(request):
    data = Module.objects.all()
    serializer = ModuleSerializer(data, many=True)
    return Response(serializer.data)

