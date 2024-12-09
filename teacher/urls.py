
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   path('assignment/', views.assignment_page, name='assignment_page'), 
   path('instructor_page', views.instructor, name='instructor'), 


]
