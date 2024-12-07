from django.shortcuts import render,redirect
from .models import login
from .forms import auto_form,LoginForm
from django.views import View

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'index.html')
def index2(request):
    if request.method=='POST':
        n=request.POST['a']
        p=request.POST['b']
        data=login(username=n,password=p)
        data.save()
    return render(request,'index2.html')
'''
#autoform
def adding(request):
    data={
        'values':auto_form()
    }
    if request.method=='POST':
        values=auto_form(request.POST)
        if values.is_valid():
            values.save()
    return render(request,'adding.html',data)
'''

class addingview(View):
    def get(self,request):
        print("class based get")
        data={
        'values':auto_form()
        }
        return render(request,'adding.html',data)
    def post(self,request):
        print("class based post")
        if request.method=='POST':
            values=auto_form(request.POST)
        if values.is_valid():
            values.save()
        return redirect('/adding/')



def select(request):
    datas=login.objects.all()
    return render(request,'select.html',{'values':datas})
def deletelogin(request,id):
    data=login.objects.get(id=id)
    data.delete()
    return redirect('/select/')

#update
def updatelogin(request,id):
    data=login.objects.get(id=id)
    dt={
        'updatevalue':auto_form(instance=data)
    }
    if request.method=='POST':
        updatevalue=auto_form(request.POST,instance=data)
        if updatevalue.is_valid():
            updatevalue.save()
            return redirect('/select/')
    return render(request,'updatevalue.html',dt)


def registration(request):
    if request.method=='POST':
        user_form=UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponse("<h1>registration successfull</h1>")
    else:
        user_form=UserCreationForm()
    return render(request,'register.html',{'user':user_form})


def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('<h1>login successfull</h1>')
                else:
                    return HttpResponse('<h1>invalid account</h1>')
            else:
                return HttpResponse('<h1>Enter valid details</h1>')
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponse('<h1>logout successfull</h1>')
