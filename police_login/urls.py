from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [path('',views.police_login,name='police_login'),
               path('fetch',views.fetch,name='fetch'),
               path('register',views.register,name='register'),
               path('new',views.new,name='new'),
               path('tables',views.d_tables,name='tables'),
               path('dashboard',views.d_dashboard,name='dashboard'),
               path('map',views.d_map,name='map'),
               path('about',views.d_about,name='about')

]
