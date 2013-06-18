# coding: utf-8
        
from django.contrib import admin
from django.db.models import TextField
from django.forms import Textarea

from .models import Task

admin.site.register(Task)

