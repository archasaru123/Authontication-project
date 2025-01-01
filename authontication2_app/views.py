from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
def  signup(request):
   
    if request.method=='POST':
         username=request.POST['username']
         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email = request.POST['email']
         password= request.POST['password']
         password2 = request.POST['password2']
         if password == password2: 
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return redirect('signin')
         else:
               messages.info(request,"password not matching")
               return redirect('/')
         

    return render(request,"register.html")
def signin(request):
    
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,"invalid details")
            return redirect('signin')
    else:
        return render(request,'login.html')
def home(request):
       return render(request,'home.html')                                                                                                             
    
def logout(request):
        auth.logout(request)
        return redirect('signin')  



