from django.shortcuts import render
from main.models import UserAcc


def index(request):
    all_users = UserAcc.objects.all()
    context = {"data":all_users.nameсв }

    return render(request,"index.html",context)