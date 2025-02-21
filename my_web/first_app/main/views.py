from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "index.html",context)

def blog(request):
    context = {}
    return render(request, 'blog.html',context )
def index_2(request):
    context = {}
    return render(request,'index-2.html',context)
def single_blog(request):
    context = {}
    return render(request, 'single-blog.html',context)
def flighter(request):
    context = {}
    return render(request, 'fighter.html',context)
def team(request):
    context = {}
    return render(request, 'team.html',context)
def elements(request):
    context = {}
    return render(request, 'elements.html',context)
def content(request):
    context = {}
    return render(request, 'contact.html',context)
