from django.shortcuts import render, redirect
from tst.forms import RegForm
from django.http import HttpResponse
import json
from tst.models import Resp, Results
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
def register(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            roll_no = form.cleaned_data['roll_no']
            name = form.cleaned_data['name']
            passkey = form.cleaned_data['passkey']
            form.save()
            return redirect('questions', roll_no, passkey)

    else:
        form = RegForm()
    return render(request, 'tst/register.html', {'form': form})

from django.db.models import Q

@cache_control(no_cache=True, must_revalidate=True)
def questions(request, ids, psk):
    json_file = open('C:\\Users\\anthi\\OneDrive\\Documents\\quiz\\quiz\\tst\\static\\tst\\questions.json', 'r')
    q = json.load(json_file)
    dict_ques = q[q[psk]]
    ans = ""
    if request.method == "POST":
        for key,value in dict_ques.items():
            ans = ans + str(request.POST.get(key))
            criterion1 = Q(roll_no = ids)
            criterion2 = Q(passkey = psk)
            q = Resp.objects.filter(criterion1 & criterion2).update(resp = ans)
        return render(request, 'tst/end.html')
    return render(request, 'tst/questions.html', {'dict_ques': dict_ques})


def results(request):
    if request.method == "POST":
        key = request.POST.get("key")
        json_file = open('C:\\Users\\anthi\\OneDrive\\Documents\\quiz\\quiz\\tst\\static\\tst\\questions.json', 'r')
        q = json.load(json_file)
        s = "ans_" + key
        ans = q[s]
        resu = []
        all_entries = Resp.objects.all().filter(passkey = key)
        for i in all_entries:
            roll_no = i.roll_no
            name = i.name
            resp = i.resp
            count = 0
            for i in range(len(ans)):
                if resp[i] == ans[i]:
                    count+=1
            resu.append([roll_no, name, count])
        return render(request, "tst/show_results.html", {'l': resu})
    return render(request, "tst/results.html")
