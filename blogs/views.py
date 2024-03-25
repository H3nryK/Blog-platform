from django.shortcuts import render, redirect
from .models import *

def upload_blogs(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        picture = request.POST.get('image')

        blogs, created = Blogs.objects.get_or_create(title=title, content=content, picture=picture)

        return redirect('blogs')
    
    return render(request, 'uploads.html')

def list_blogs(request):
    blogs = Blogs.objects.all()
    return render(request, 'blogs.html', {'blogs':blogs})