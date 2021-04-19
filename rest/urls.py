from django.urls import path
from . import views

urlpatterns = [path('emergency',views.emergency,name='police_login'),
               path('intimate',views.intimate,name='police_login'),
               path('report',views.report,name='police_login'),
               path('intimation_stat',views.intimation_stat,name='intimation_stat')]