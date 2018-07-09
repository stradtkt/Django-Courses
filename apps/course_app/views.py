# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import Course
# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, 'course_app/index.html', context)

def add_course(request):
    name = request.POST['name']
    description = request.POST['description']
    course = Course.objects.create(name=name, description=description)
    return redirect('/')

def destroy(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('/')