
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [

    path('error/', views.error, name='error'),
    path('blog/',views.details,name='details'),
    path('blog/',views.blog,name='blog'),
    path('index/',views.index,name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/',views.service,name='service'),
    path('starter/',views.starter,name='starter'),
    path('show/',views.show,name='show'),

]
