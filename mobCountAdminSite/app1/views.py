from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.auth import authenticate, login
import os
from django.conf import settings
from desktop import Main
import subprocess
# Create your views here.

def Homepage(request):
    return render(request,'homepage.html')


def Dashboard(request):
    os.chdir(r'E:\7th Semester\FYP-1\Final Code\UAV-Based-People-Counting-ADMIN-PANEL\mobCountAdminSite\pythonProject2\yolov5-Object-Counter')
    os.system('python detect.py --weights runs/train/exp4/weights/best.pt --img 640 --conf 0.25 --source ../data/ --print_class head')
    os.chdir(r'E:\7th Semester\FYP-1\Final Code\UAV-Based-People-Counting-ADMIN-PANEL\mobCountAdminSite')
    return render(request,'dashboard.html')

# def count_people(request):
#     with open('count.txt', 'r') as f:
#         count = int(f.read())
#     context = {'count': count}
#     return render(request, 'dashboard.html', context)

def count_people(request):
    count = 12
    uploaded_image_path = ''
    if request.method == 'POST':
        image = request.FILES['image']
        # do whatever you need with the uploaded image here
        img = Image.open(image)
        uploaded_image_path = image.name
        count = 5  # for demo purposes only, replace with your own logic
        # save the uploaded image to the media directory
        file_path = os.path.join(settings.MEDIA_ROOT, uploaded_image_path)
        with open(file_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
    # construct the URL of the uploaded image
    uploaded_image_url = os.path.join(settings.MEDIA_URL, uploaded_image_path)
    context = {'count': count, 'uploaded_image_url': uploaded_image_url}
    return render(request, 'dashboard.html', context)

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password1')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            Main.main_window()

            return redirect('dashboard')
    return render(request,'mainPage.html')

def SignupPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        username=request.POST.get('user')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2') 
        my_user=User.objects.create_user(username,email,pass1)
        my_user.save()

    return render(request,'mainPage.html')


