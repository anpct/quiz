from django.shortcuts import render, redirect
from tst.forms import RegForm
from django.http import HttpResponse
import json
from user.models import Resp
from django.views.decorators.cache import cache_control
from django.db.models import Q

@cache_control(no_cache=True, must_revalidate=True)
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
        return render(request, 'tst/end.html')
    return render(request, 'tst/questions.html', {'dict_ques': dict_ques})


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
            roll_no = i.roll_no
            name = i.name
            resp = i.resp
            count = 0
            for i in range(len(ans)):
                if resp:
                    if resp[i] == ans[i]:
                        count+=1
            resu.append([roll_no, name, count])
        return render(request, "tst/show_results.html", {'l': resu})
    return render(request, "tst/results.html")
