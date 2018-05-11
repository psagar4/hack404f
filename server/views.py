import json

from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from server.models import Movies, Credits
from server.apps import ServerConfig
from django.http import HttpResponse

from django.apps import apps

#import http.client
import requests
import base64

username = '1'

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('/home/')

@csrf_exempt
def login_form(request):
    return render(request, 'login.html', {})

@csrf_exempt
def login_user(request):
    global username
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    username = '1'
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('success')
    print("Can't authenticate")
    return redirect(settings.LOGIN_URL, request)


@csrf_exempt
def search(request):
    movie = Movies.objects.get(movie_id=int(request.GET['id']))
    
    movie_obj = json.loads(str(movie))

    del movie_obj['genres']

    conf = apps.get_app_config('server')
    print(conf.algo_svd)

    credits = Credits.objects.filter(movie_id_id=int(request.GET['id']))


    ls = []
    if int(request.GET['id']) == 313369:
        #Gosling
        tup = conf.algo_svd.predict(uid=conf.trainset.to_raw_uid(int(username)), iid=conf.trainset.to_raw_iid(104329))
        dd = dict()
        dd['rating'] = str(tup[3])
        dd['actor'] = Credits.objects.get(credit_id=int(tup[1])).getname()
        ls.append(dd)
    else:
        for credit in credits:
            tup = conf.algo_svd.predict(uid=conf.trainset.to_raw_uid(int(username)), iid=conf.trainset.to_raw_iid(int(str(credit))))
            print(tup[0], tup[1], tup[2], tup[3], tup[4])
            dd = dict()
            dd['rating'] = str(tup[3])
            dd['actor'] = Credits.objects.get(credit_id=int(tup[1])).getname()
            ls.append(dd)
        

    #connection = http.client.HTTPSConnection('10.177.64.134:9000')
    #headers = {'Content-type': 'application/json'}

    #onnection.request('POST', '/', json.dumps(ls), headers)

    #response = connection.getresponse()
    #print(response.read().decode())

    r = requests.post('http://10.177.64.134:9000', data = json.dumps(ls))
    print(r.content)

    fh = open("/Users/psagar/workspace/Hack_404/app/ryan.png", "wb")

    fh.write(base64.b64decode(r.content))
    fh.close()

    movie_obj['imgUrl'] = "../images/ryan.png"

    return HttpResponse(json.dumps(movie_obj))
