# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
from django.core.urlresolvers import reverse


def index(request):
    courses = Course.objects.all()
    context = {
        "courses": courses
    }
    return render(request, 'course_app/index.html', context)

def add_course(request):
    errors = Course.objects.validate_course(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect(reverse('courses:add_course_page'))
    else:
        name = request.POST['name']
        description = request.POST['description']
        Course.objects.create(name=name, description=description)
        messages.success(request, 'Course Added Successfully')
        return redirect(reverse('courses:home'))

def add_course_page(request):
    return render(request, 'course_app/add-course.html')

def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect(reverse('courses:home'))

def subjects(request, id):
    course = Course.objects.get(id=id)
    subjects = Subject.objects.filter(course=course)
    context = {
        "subjects": subjects,
        "course": course,
    }
    return render(request, 'course_app/subjects.html', context)

def add_subject(request, id):
    errors = Course.objects.validate_course(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect(reverse('courses:subjects'))
    else:
        title = request.POST['title']
        description = request.POST['description']
        course = Course.objects.get(id=id)
        courses = Subject.objects.get(course=course)
        Subject.objects.create(title=title, description=description, course=courses)
        messages.success(request, 'Added Subject')
        return redirect(reverse('courses:subjects'))