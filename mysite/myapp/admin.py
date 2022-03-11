from django.contrib import admin

from .models import Module, Professor
admin.site.register(Professor)
admin.site.register(Module)

# Register your models here.
