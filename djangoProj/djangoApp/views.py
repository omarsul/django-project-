
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
import bcrypt 
from djangoApp.models import User

def index(request):

    return render(request, "login.html")

def register(request):

    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('')
    else:

        
        user = User()
        user.name = request.POST['name']
        user.alias = request.POST['alias']
        user.email = request.POST['email']
        password = request.POST['password']
        user.birthDate = request.POST['date']
        user.password = hash.decode()
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode(),salt)
        user.save()
        messages.success(request, "successfully registred")
        # redirect to a success route
        return redirect('index')
    

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user=User.objects.get(email=email)
            if bcrypt.checkpw(password.encode(),user.password.encode()):
                request.session["userId"]=user.id
                return redirect('friends')
            else:
                return redirect('')
        except User.DoesNotExist:
            print("no user exist")
            return redirect('')
    return render(request, "login.html")

def friendsTable(request):
    if "userId" not in request.session:
        return HttpResponse("login first")
    user = User.objects.get(id=request.session["userId"])
    others = User.objects.exclude(id=request.session["userId"])
    friends = user.friends.all()
    context = {
        "loged": user,
        "others": others,
        "friends": friends
    }
    return render(request, "friendsTable.html",context)

def profile(request,Userid):
    context = {
        "profile": User.objects.get(id=Userid)
        
    }
    return render(request, "profile.html", context)

def delete(request,Userid):
    d = User.objects.get(id=Userid)
    d.delete()
    return redirect("friends")

def add(request,Userid):
    user = User.objects.get(id=request.session["userId"])
    user.friends.add(Userid)
    return redirect("friends")
