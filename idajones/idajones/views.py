from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from user_detail.models import user_detail
from signup.models import signup

def login_page(request):
    return render(request,"loggin1.html")
def home_page(request):
    return render(request, "home.html")
def signup_page(request):
    return render(request, "signup.html")
def signup(request):
    message=''
    if request.method=="POST":
        name=request.POST.get('firstname')
        mail=request.POST.get('email')
        pswd=request.POST.get('password')
        confirm_pswrd=request.POST.get('confirm_password')
        saved=signup(name=firstname,mail=email,pswd=password,confirm_pswrd=confirm_password)
        saved.save()
    return render(request, "signup_page")
def buy_detail(request):
    return render(request, "buy.html")
def save_enquary(request):
    message=''
    if request.method=="POST":
        name=request.POST.get('First_name')
        room=request.POST.get('Room_address')
        village=request.POST.get('village_address')
        city=request.POST.get('city_address')
        state=request.POST.get('state_address')
        pincode=request.POST.get('pincode_address')
        phone=request.POST.get('phone')
        altternatePh=request.POST.get('alt_phone')
        saves=user_detail( First_name=name ,room_address=room,village_address=village,city_address=city,state_address=state,pincode_address=pincode,phone=phone ,alt_phone=altternatePh)
        saves.save()
    
    return render(request,"buy.html")