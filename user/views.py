from django.shortcuts import render
from .models import User


# Create your views here.
def login(request):
    if request.method == "GET":
        print("getzhixing")
        return render(request, 'user/user_login.html')
    elif request.method == "POST":
        print("postzhixing")
        print(request.POST.get("username"))
        print(request.POST.get("password"))

    return render(request, 'user/user_login.html')


def register(request):
    return render(request, 'user/user_register.html')


def all_user(request):
    return render(request, 'user/user_all_user.html')


def personal_information(request):
    return render(request, 'user/personal_information.html')
