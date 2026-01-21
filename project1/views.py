from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def project(request):
    return render(request, "project.html")

def led(request):
    return render(request, "led.html")

def counter(request):
    if(request.method == "POST"):
        data = request.POST
        result = data.get('result')

        if result == "":
            result = 0
        else:
            result = int(data.get('result'))
        if('increment' in request.POST):
            result += 1
            return render(request, "counter.html", context={'result': result})
        if('decrement' in request.POST):
            result -= 1
            return render(request, "counter.html", context={'result': result})
        if('reset' in request.POST):
            result = 0
            return render(request, "counter.html", context={'result': result})
    return render(request, "counter.html")
        
def calci(request):
    if(request.method=="POST"):
        data=request.POST
        num1=data.get("num1")
        num2=data.get("num2")
        operation=data.get("operation")
        if num1 =="" or num2=="":
            result="Please provide both numbers"
            return render(request, "calci.html", context={"result": result})
        else:
            num1=int(data.get("num1"))
            num2=int(data.get("num2"))
            if operation=="add":
                result=num1+num2
                return render(request, "calci.html", context={"result": result})
            if operation=="subtract":
                result=num1-num2
                return render(request, "calci.html", context={"result": result})
            if operation=="multiply":
                result=num1*num2
                return render(request, "calci.html", context={"result": result})
            if operation=="divide":
                if num2==0:
                    result="Cannot divide by zero"
                    return render(request, "calci.html", context={"result": result})
                else:
                    result=num1/num2
                    return render(request, "calci.html", context={"result": result})
    return render(request, "calci.html")

def index(request):
    return render(request, "index.html")

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=User.objects.filter(username=username)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
          login(request,user)
          return redirect('index')
        else:
          result="Password Entered is wrong"
          return HttpResponse ("Username or Password is incorrect!!!")
  
    return render (request,'login.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')
    
          
    
def singup(request):
    # compatibility wrapper for URL imports that expect `singup`
    return SignupPage(request)

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def predict(request):
    if(request.method=="POST"):
        data=request.POST
        area=int(data.get('textarea'))
        rooms=int(data.get('textroom'))
        age=int(data.get('textage'))
        if('predict' in request.POST):
            import pandas as pd
            path="/Users/hemantkumarrudramuni/Downloads/Datanew/homeprices_Mul.csv"
            data=pd.read_csv(path)
            medianval=data.bedrooms.median()
            data.bedrooms=data.bedrooms.fillna(medianval)
            inputs = data.drop(columns=["price"])
            output = data["price"]
            import sklearn 
            from sklearn import linear_model
            model=linear_model.LinearRegression()
            model.fit(inputs,output)
            result=model.predict([[area,rooms,age]])
            return render(request,'predict.html',context={'result':result})
    return render(request,"predict.html")



