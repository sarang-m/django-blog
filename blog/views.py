from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts =[
    {
        'name' : 'Name1',
        'id' : '1',
        'content' : 'first content'
    },
    {
        'name' : 'Name2',
        'id' : '2',
        'content' : 'second content'
    },
    {
        'name' : 'Name3',
        'id' : '3',
        'content' : 'third content'
    },
    
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')