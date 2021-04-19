from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import hashlib
from .models import hell
# Create your views here.
def home(request):
    #print(request)
    s='hell'
    #return HttpResponse('<h1>fun</h1>')
    return render(request,'home.html',{'name':"11"})
def add(request):
    val1=float(request.POST['num1'])
    val2=float(request.POST['num2'])
    data={'lattitude': val1, 'longitude': val2}
    return render(request,'result.html',{'lat':val1,'lon':val2})
    #return JsonResponse(data)
@csrf_exempt
def req(request):
    data = {"employees": [{"firstname": "John", "age": 30, "mail": "john@gmail.com"},
                          {"firstname": "Jimmy", "age": 25, "mail": "jimmy@gmail.com"},
                          {"firstname": "Jenny", "age": 22, "mail": "jenny@gmail.com"},
                          {"firstname": "Jeremy", "age": 40, "mail": "jeremy@gmail.com"},
                          {"firstname": "Justin", "age": 32, "mail": "justin@gmail.com"}]}
    if request.method=='POST':
        try:
            print(request.POST['username'])
            print(request.POST['mobile'])
            print(request.POST['dob'])
            print(request.POST['district'])
            print(request.POST['area'])
            print(request.POST['pin'])
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
        return JsonResponse(data)
    if request.method=='GET':
        return JsonResponse(data)
def police(request):
    return render(request,'login.html')