from django.shortcuts import render,HttpResponse
from django import forms


# Create your views here.
def add(request):
    
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})

def home(request):

    return render (request,'home.html',{'name':'Avijit Patra',
    'location':'Kirnahar',
    'gender':'male',
    'college':'BC Roy',
    'company':'IBM',
    'age':'26',
    'bik':'Mt-15',
    'passion':'code',
    'type':'good',})
