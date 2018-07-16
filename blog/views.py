from django.shortcuts import render,get_object_or_404
from .models import Blog

def blog(request):
    blog = Blog.objects
    return render(request,'blog/blog.html',{'blogs':blog})

def detail(request,blog_id):
    detailblog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'blog/detail.html',{'detailblog':detailblog})