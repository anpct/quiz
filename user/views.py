
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, PkForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':

        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
 
    else:
        f = CustomUserCreationForm()
        request.session.flush()
        return render(request, 'tst/signup.html', {'form': f})



def login_request(request):
    if request.method == 'POST':
        
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('pk')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    request.session.flush()
    return render(request = request,
                    template_name = "tst/login.html",
                    context={"form":form})

@login_required
def get_pk(request):
    if request.method == 'POST':
        form = PkForm(request.POST)
        if form.is_valid():
            request.session["passkey"] = form.cleaned_data.get('passkey')
            u = Resp(user = request.user, passkey = form.cleaned_data.get('passkey'))
            u.save()
            return redirect('questions')
    form = PkForm()
    return render(request, 'tst/pk.html', {"form":form})

from django.shortcuts import render, redirect
from tst.forms import RegForm
from django.http import HttpResponse
import json
from user.models import Resp
from django.views.decorators.cache import cache_control
from django.db.models import Q

@login_required
def questions(request):
    json_file = open('tst\\static\\tst\\questions.json', 'r')
    q = json.load(json_file)
    dict_ques = q[q[request.session["passkey"]]]
    ans = ""
    if request.method == "POST":
        for key,value in dict_ques.items():
            ans = ans + str(request.POST.get(key))
            criterion1 = Q(user = request.user)
            criterion2 = Q(passkey = request.session["passkey"])
            q = Resp.objects.filter(criterion1 & criterion2).update(resp = ans)
        del request.session["passkey"]
        logout(request)
        return render(request, 'tst/end.html')
    return render(request, 'tst/questions.html', {'dict_ques': dict_ques})

@login_required
def results(request):
    if request.method == "POST":
        key = request.POST.get("key")
        json_file = open('tst\\static\\tst\\questions.json', 'r')
        q = json.load(json_file)
        s = "ans_" + key
        ans = q[s]
        resu = []
        all_entries = Resp.objects.all().filter(passkey = key)
        for i in all_entries:
            roll_no = i.user
            name = None
            resp = i.resp
            count = 0
            for i in range(len(ans)):
                if resp:
                    if resp[i] == ans[i]:
                        count+=1
            resu.append([roll_no, name, count])
        return render(request, "tst/show_results.html", {'l': resu})
    return render(request, "tst/results.html")
