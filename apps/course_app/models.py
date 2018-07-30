# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CourseManager(models.Manager):
    def validate_course(self, postData):
        errors = {}
        if len(postData['name']) < 6:
            errors['name'] = "You need to add at least 6 characters for the name"
        if len(postData['description']) < 10:
            errors['description'] = "You need at least 10 characters for the description"
        return errors

        
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class SubjectManager(models.Manager):
    def validate_subject(self, postData):
        errors = {}
        if len(postData['title']) < 5:
            errors['title'] = "Title needs to be 5 or more characters"
        if len(postData['description']) < 10:
            errors['description'] = "Description needs to be 10 or more characters"
        return errors

class Subject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Course, related_name="course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SubjectManager()