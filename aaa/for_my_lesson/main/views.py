from pyexpat.errors import messages

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Article
from .forms import ArticleForm

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
#
# def createE(request):
#     context = {}
#     if request.method == "POST":
#         Article.objects.create(title=request.POST['title'],content=request.POST['content'],image=request.POST['image'])
#     return render(request,'create.html',context)

def create(request):
    data = Article.objects.all()
    form = ArticleForm(request.POST, files=request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('main;blogs')
        messages.succ
    context = {
        'data': data,
        "form": form
    }
    return render(request,'create.html',context)

def delete(request,pk):
    article = Article.objects.get(id=pk)
    context = {"date":article}

    if request.method == 'POST':
        article.delete()
        return redirect("main:blogs")
    return render(request,'delete.html',context)
