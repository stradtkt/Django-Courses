from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^add_course$', views.add_course, name="add_course"),
    url(r'^add-course-page$', views.add_course_page, name="add_course_page"),
    url(r'^(?P<id>\d+)/delete_course$', views.delete_course, name="delete_course"),
    url(r'^(?P<id>\d+)/subjects', views.subjects, name="subjects"),
]