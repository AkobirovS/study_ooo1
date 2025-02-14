from django.shortcuts import render
from main.models import UserAcc,Blogs


def index(request):
    all_users = UserAcc.objects.all()
    # addthenew = UserAcc(name="sardor",surname="Akonirovs")
    # addthenew.save()
    # UserAcc.objects.create(name="Akobir",surname="Asrorivich")
    # print(all_users)
    context = {"data":all_users}

    return render(request,"index.html",context)



def blogs(request):
    all_infos = Blogs.objects.all()
    contxt = {"date":all_infos}

    return render(request, "blogs.html",contxt)


def details(request,pk):
    blods = Blogs.objects.get(id=pk)
    print(blods)
    context = {"object":blods}

    return render(request,"detayle.html",context)