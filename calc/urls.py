from django.urls import path
from .import views
urlpatterns=[path('',views.home,name='home'),
path('add',views.add,name='add'),path('req',views.req,name='req'),path('police',views.police,name='police')]