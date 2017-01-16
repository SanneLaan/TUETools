from django.contrib import admin
from .models import Course, Document
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

DOCUMENT_FILE_TYPES = ['doc', 'docx', 'pdf']

admin.site.register(Course)
admin.site.register(Document)