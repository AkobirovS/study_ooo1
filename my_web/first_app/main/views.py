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