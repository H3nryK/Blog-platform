from django.shortcuts import render, redirect, get_object_or_404
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
    blogs = Blogs.objects.all().order_by('-uploaded_on')
    return render(request, 'blogs.html', {'blogs':blogs})

def detail_blogs(request, blog_id):
    blog_post = get_object_or_404(Blogs, id=blog_id)
    return render(request, "blog-details.html", {"blog_post": blog_post})