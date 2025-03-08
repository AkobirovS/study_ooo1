from django.shortcuts import render, get_object_or_404
from .models import Article

def base(request):
    context = {"date":Article}

    return render(request,'index.html',context)

def blogs(request):
    date = Article.objects.all()
    context = {"date":date}

    return render(request, 'blog.html',context)

def detail(request, pk):
    # all_objects = Article.objects.get(id=pk)
    all_objects = get_object_or_404(Article, id=pk)
    content = {'data':all_objects}

    return render(request,"detail.html",content)