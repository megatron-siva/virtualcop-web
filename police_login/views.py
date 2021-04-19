from django.shortcuts import render
from django.http import HttpResponse

from rest.models import emergency_information,report_information,intimate_information
from .models import POLICE_LOGIN
from django.apps import apps
import hashlib

def police_login(request):
    return render(request,'login.html')
def fetch(request):
    #i=intimate_information.objects.all()
    i=2
    e=len(emergency_information.objects.all())
    r=len(report_information.objects.all())

    a=POLICE_LOGIN.objects.all()
    for i in a:
        if i.username==str(request.POST['username']) and i.password==(hashlib.md5(str(request.POST['pass']).encode()).hexdigest()):
            i = len(intimate_information.objects.all())
            e = len(emergency_information.objects.all())
            r = len(report_information.objects.all())
            #return render(request, 'emergency_map.html', {'data': data,'status':status,'tittle':'victim position'})
            return render(request,'dashboard/dashboard.html',{'police_tab':a,'i':i,'e':e,'r':r})
    return render(request,'login.html')
def register(request):
    name=str(request.POST['username'])
    password=str(request.POST['pass'])
    password_con=str(request.POST['pass_con'])
    district_=str(request.POST['district'])
    state_=str(request.POST['state'])
    print(name,password,password_con)
    if password==password_con:
        hash1 = hashlib.md5(password.encode())
        new_login=POLICE_LOGIN(username=name,password=hash1.hexdigest(),district=district_,state=state_)
        new_login.save()
        return render(request,'login.html')
    else:
        return render(request,'register.html')
def new(request):
    return render(request,'register.html')
def d_tables(request):
    e=emergency_information.objects.all()
    f=report_information.objects.all()
    return render(request,'dashboard/tables.html',{'e_data':e,'r_data':f})
def d_dashboard(request):
    a = POLICE_LOGIN.objects.all()
    return render(request,'dashboard/dashboard.html',{'police_tab':a})
def d_map(request):
    data=emergency_information.objects.all()
    for i in data:
        if i.username!=None:
            status=True
        else:
            data=None
            status=False
    return render(request, 'dashboard/map.html', {'data': data,'status':status,'tittle':'victim position'})
def d_about(request):
    base=[{'id':6,'name':'Megatron $iva','email':'sivappriyansandeep@gmail.com'},]
    return render(request,'dashboard/about.html',{'data':base})