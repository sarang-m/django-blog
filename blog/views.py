from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

posts =[
    {
        'title' : 'Name1',
        'auther' : '1',
        'date' : '27-2-2021',
        'content' : 'first content'
    },
    {
        'title' : 'Name2',
        'auther' : '2',
        'date' : '28-2-2021',
        'content' : 'second content'
    },
    {
        'title' : 'Name3',
        'auther' : '3',
        'date' : '29-2-2021',
        'content' : 'third content'
    },
    
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})