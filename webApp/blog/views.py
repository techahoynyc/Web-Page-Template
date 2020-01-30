from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'JamesB',
        'title': 'Space Laughs',
        'content': 'Scify',
        'Date': 'Jan. 28th, 2020'
    },
    {
        'author': 'Jane',
        'title': 'ShakeySpeare',
        'content': 'Classic',
        'Date': 'Jan. 28th, 2005'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


    
