from django.urls import path
from django.conf.urls import url
from . import views
app_name ='mark'
urlpatterns = [
    path('',views.hello_temp,name='hello_temp'),
    path('download/',views.download,name='download'),
]
