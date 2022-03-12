from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from genrator.models import Contact
from django.contrib import messages
import random

# Rest api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contact
from .serializers import contactserializer


#Rest api

class contactlist(APIView):
    def get(self,request):
        contactdetail = Contact.objects.all()
        serialize = contactserializer(contactdetail,many=True)
        return Response(serialize.data)
    
    def post(self):
        pass

# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def about(request):
    return render(request,'generator/about.html')


def password(request):
    thepass = ""
    charecters = list('abcdefghijklmniopqrstuvwxyz')
    if request.GET.get('numbers'):
        charecters.extend('0123456789')

    if request.GET.get('uppercase'):
        charecters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if request.GET.get('special'):
        charecters.extend('!@#$%^&*')

    length0 = int(request.GET.get('length'))
    print(length0)

    for i in range(length0):
        thepass += random.choice(charecters)
        

    return render(request,'generator/password.html',{'password0':thepass})

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        Email = request.POST.get('Email')
        Phone = request.POST.get('Phone')
        desc = request.POST.get('desc')
        Date = request.POST.get('Date')
        contact = Contact(Name=Name,Email=Email,Number=Phone,Text_area=desc,Date=Date)
        contact.save()
        messages.success(request, 'Succesfully Submitted.')
    return render(request,'generator/contact.html')

