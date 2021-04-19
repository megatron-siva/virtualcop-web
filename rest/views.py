from django.shortcuts import render
from django.http import JsonResponse
from .models import emergency_information,intimate_information
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.
@csrf_exempt
def emergency(request):
    try:
        print(request.POST['username'])
        print(request.POST['mobile'])
        print(request.POST['dob'])
        print(request.POST['address'])
        print(request.POST['pname'])
        print(request.POST['pmob'])
        print(request.POST['prelation'])
        print(request.POST['p2name'])
        print(request.POST['p2mob'])
        print(request.POST['p2relation'])
        print(request.POST['latitude'])
        print(request.POST['longitude'])


    except:
        pass
    new=emergency_information(username=str(request.POST['username']),mobile=str(request.POST['mobile']),dob=request.POST['dob'],address=request.POST['address'],pname=request.POST['pname'],pmob=int(request.POST['pmob']),prelation=request.POST['prelation'],p2name=request.POST['p2name'],p2mob=int(request.POST['p2mob']),p2relation=request.POST['p2relation'],latitude=request.POST['latitude'],longitude=request.POST['longitude'])
    new.save()

    return JsonResponse({'data':'received'})
@csrf_exempt
def intimate(request):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization": "fRqGhD7Hb5YAv9ptMnwCZBgeXil8ykxmWsNELIrJcjUSO6102TiHz89I6nDdbQFR2tWVpXxYCaBZ0JAc",
                   "sender_id": "FSTSMS", "message":"Your  "+str(request.POST['prelation'])+' '+str(request.POST['username']), "language": "english", "route": "p",
                   "numbers": str(request.POST['pmob'])+','+str(request.POST['p2mob'])}
    print(str(request.POST['pmob'])+','+str(request.POST['p2mob']))

    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    new = intimate_information(username=str(request.POST['username']), mobile=str(request.POST['mobile']),
                                dob=request.POST['dob'], address=request.POST['address'], pname=request.POST['pname'],
                                pmob=int(request.POST['pmob']), prelation=request.POST['prelation'],
                                p2name=request.POST['p2name'], p2mob=int(request.POST['p2mob']),
                                p2relation=request.POST['p2relation'], latitude=request.POST['latitude'],
                                longitude=request.POST['longitude'])
    new.save()

    return JsonResponse({'data': 'received'})
    pass
@csrf_exempt
def report(request):
    pass
def intimation_stat(request):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    #print(int(current_time[6:]))
    return JsonResponse({'second':int(current_time[6:]),'time':str(current_time)})
    pass
class status:
    pass
