from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")
def home(request):
    user = request.user
    if user.is_anonymous!=True:
        pro = UserProfile.objects.get(user=user)
        name = user.first_name
        surname = user.last_name
        return render(request,"home.html",{"fullname":name+" "+surname,"location":pro.location,"status":pro.status,"pic":pro.pic})
    else:
        return redirect("index")

def profile(request):
    user = request.user
    if user is not None:
        pro = UserProfile.objects.get(user=user)
        name = user.first_name
        surname = user.last_name
        return render(request,"profile.html",{"fullname":name+" "+surname,"location":pro.location,"status":pro.status,"pic":pro.pic})
    else:
        return redirect("index")

def Login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("profile")
        else:
            return redirect("index")
    else:
       return render(request,"index.html") 

def Logout(request):
    logout(request)
    return redirect("index")

def Register(request):
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        location = request.POST["location"]
        status = request.POST["status"]
        image = request.POST["image"]

        user = User.objects.create_user(username=username)
        user = User.objects.get(username=username)
        user.set_password(password)
        user.is_staff = True
        user.save()

        u = UserProfile.objects.create(user=user)
        u.location = location
        u.status = status
        u.pic = image
        u.save()


        return redirect("index")
    else:
        return redirect("index")







