from django.shortcuts import HttpResponse
from django.shortcuts import render
from cmdb import models
user_list = [
    {"user": "A", "pwd": "123"},
    {"user": "B", "pwd": "456"}
]

def index(request):
    if request.method == 'POST':
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        print(username, password)
        temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)
        user_list = models.UserInfo.objects.all()
    return render(request, 'index.html',{"data": user_list})