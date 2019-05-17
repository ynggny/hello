from django.http import HttpResponse
from django.http.response import HttpResponse
from django.template import loader
from wow.tango import fusion
import csv
from django.shortcuts import render
from .models import Stu

def hello_temp(request):
    return render(request,'mark/index.html')

def download(request):
    #with open(response,'w',encoding='utf_8_sig') as response:
    response = HttpResponse(content_type='text/csv;charset=utf_8_sig')
    response['Content-Disposition']='attachment; filename=shine.csv'
    writer=csv.writer(response)
    writer.writerows(fusion())
    return response
