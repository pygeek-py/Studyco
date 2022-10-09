from django.shortcuts import render, get_object_or_404, redirect
from .forms import registerform, imgform, boxform
from .models import movieimg, list, box, talk, followercount
from .filters import boxfilter, userfilter
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import threading
import datetime
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = registerform()
    return render(request, "base/register.html", {"form":form})
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
            "massage": "invalid credentials"
            })
    return render(request, ("base/login.html"))
    

def logout_view(request):
    logout(request)
    return render(request, "base/login.html", {
    "message":"Logged out"
    })


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    lis = list.objects.all()
    boxs = box.objects.all().order_by('-id')
    boxse = box.objects.filter(person=peo).order_by('-id')[0:1]
    mov = movieimg.objects.all()
    boxnum = box.objects.all().count()
    tall = talk.objects.all().order_by('-id')[0:3]
    myFilter = boxfilter(request.GET, queryset=boxs)
    boxs = myFilter.qs
    time = datetime.datetime.now()
    return render(request, ('base/home.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'lis': lis,
        'boxs': boxs,
        'boxse': boxse,
        'mov': mov,
        'boxnum': boxnum,
        'tall': tall,
        'filter': myFilter,
        'time': time
    })

def seeall(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    lis = list.objects.all()
    boxs = box.objects.all().order_by('-id')
    boxse = box.objects.filter(person=peo).order_by('-id')[0:1]
    mov = movieimg.objects.exclude(user=peo).order_by('-id')
    boxnum = box.objects.all().count()
    tall = talk.objects.all().order_by('-id')[0:3]
    myFilter = userfilter(request.GET, queryset=mov)
    mov = myFilter.qs
    time = datetime.datetime.now()
    usera = User.objects.exclude(username=request.user.username).order_by('-id')
    return render(request, ('base/seeall.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'lis': lis,
        'boxs': boxs,
        'boxse': boxse,
        'mov': mov,
        'boxnum': boxnum,
        'tall': tall,
        'filter': myFilter,
        'time': time,
        'usera': usera
    })

def editprofile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    userb = request.user.username
    use = request.user.first_name
    tyd = request.user
    prof = movieimg.objects.filter(user=tyd).order_by('-id')[0:1]
    form = imgform()
    return render(request, ('base/edit.html'), {
        'user': userb,
        'use': use,
        'form': form,
        'prof': prof
    })


def work(request):
    tyd = request.user
    prof = movieimg.objects.filter(user=tyd)
    if request.method == 'POST':
        form = imgform(request.POST, request.FILES)
        if form.is_valid():
            der = form.save(commit=False)
            der.user = tyd
            der.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("home"))


def message(request, pk, topic):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    alk = box.objects.get(id=pk)
    tap = alk.talk_set.all()
    return render(request, ('base/chat.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'alk': alk,
        'tap': tap
    })

def sec(request, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("started"))
    if request.method == 'POST':
        join = box.objects.get(id=pk)
        peop = request.user
        hosts = get_object_or_404(movieimg, id=request.POST.get('prof_id'))
        text = request.POST['comm']
        free = talk(join=join, people=peop, text=text)
        free.save()
        free.host.add(hosts)
        return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("home"))

def bring(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    form = boxform()
    return render(request, ('base/bring.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'form': boxform
    })

def pool(request, pk):
    if request.method == "POST":
        form = boxform(request.POST)
        if form.is_valid():
            fod = form.save(commit=False)
            host = get_object_or_404(movieimg, id=request.POST.get('prof_id'))
            per = request.user
            fod.topic = request.POST["topic"]
            fod.name = request.POST["name"]
            fod.description = request.POST["description"]
            fod.person = per
            fod.save()
            fod.host.add(host)
            return HttpResponseRedirect(reverse("home"))
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
        return HttpResponseRedirect(reverse("home"))


def profile(request, username, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    lis = list.objects.all()
    boxs = box.objects.filter(person=peo)
    mov = movieimg.objects.all()
    boxnum = box.objects.filter(person=peo).count()
    tall = talk.objects.filter(people=peo).order_by('-id')[0:3]
    return render(request, ('base/profile.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'lis': lis,
        'boxs': boxs,
        'mov': mov,
        'boxnum': boxnum,
        'tall': tall
    })

def profiles(request, username, first_name, pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    users = username
    uses = first_name
    user = request.user.username
    use = request.user.first_name
    peo = username
    poed = request.user
    prof = movieimg.objects.filter(user=poed).order_by('-id')[0:1]
    profe = movieimg.objects.filter(user=pk).order_by('-id')[0:1]
    lis = list.objects.all()
    boxs = box.objects.filter(person=pk)
    mov = movieimg.objects.all()
    boxnum = box.objects.filter(person=pk).count()
    tall = talk.objects.filter(people=pk).order_by('-id')[0:3]
    user_followers = len(followercount.objects.filter(user=users))
    user_following = len(followercount.objects.filter(follower=users))
    user_followers0 = followercount.objects.filter(user=users)
    user_followers1 = []
    for i in user_followers0:
        user_followers0 = i.follower
        user_followers1.append(user_followers0)
    if user in user_followers1:
        follow_but = 'unfollow'
    else:
        follow_but = 'follow'

    print(user_followers)
    if request.method == 'POST':
        value = request.POST['value']
        userb = request.POST['user']
        follower = request.POST['follower']
        if value == 'follow':
            followercnt = followercount.objects.create(follower=follower, user=userb)
            followercnt.save()
        else:
            followercnt = followercount.objects.get(follower=follower, user=userb)
            followercnt.delete()
        return HttpResponseRedirect(reverse("home"))
    return render(request, ('base/profiles.html'), {
        'user': user,
        'use': use,
        'users': users,
        'uses': uses,
        'prof': prof,
        'profe': profe,
        'lis': lis,
        'boxs': boxs,
        'mov': mov,
        'boxnum': boxnum,
        'tall': tall,
        'user_followers': user_followers,
        'user_following': user_following,
        'follow_but': follow_but
    })


def basedons(request, pk, lang):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    user = request.user.username
    use = request.user.first_name
    peo = request.user
    prof = movieimg.objects.filter(user=peo).order_by('-id')[0:1]
    lis = list.objects.all()
    lisu = list.objects.get(id=pk)
    boxs = box.objects.filter(based=pk)
    mov = movieimg.objects.all()
    boxnum = box.objects.filter(based=pk).count()
    tall = talk.objects.all().order_by('-id')[0:3]
    return render(request, ('base/basedone.html'), {
        'user': user,
        'use': use,
        'prof': prof,
        'lis': lis,
        'boxs': boxs,
        'mov': mov,
        'boxnum': boxnum,
        'tall': tall,
        'lisu': lisu
    })