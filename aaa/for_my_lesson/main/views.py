from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Article

def base(request):
    context = {"date":Article}

    return render(request,'index.html',context)

def blogs(request):
    articles = Article.objects.all()  # Загружаем все статьи
    query = request.GET.get('q')  # Получаем параметр из запроса

    if query:
        articles = Article.objects.filter(title__contains=query)
    print(query)

    context = {"date": articles}  # Теперь `articles` всегда существует

    return render(request, 'blog.html', context)

def detail(request, pk):
    # all_objects = Article.objects.get(id=pk)
    all_objects = get_object_or_404(Article, id=pk)
    content = {'data':all_objects}

    return render(request,"detail.html",content)

def create(request):
    context = {}
    if request.method == "POST":
        Article.objects.create(title=request.POST['title'],content=request.POST['content'],image=request.POST['image'])
    return render(request,'create.html',context)