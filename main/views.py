from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import application

# Create your views here.

def home(request):
    return render(request, 'index.html')


def appl_info(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            country = request.POST.get('country')
            uoc = request.POST.get('uoc')
            yos = request.POST.get('yos')
            myfile1 = request.POST.get('myfile1')
            myfile2 = request.POST.get('myfile2')
            list_att = [fname, email, phone, address, country, uoc, yos, myfile1, myfile2]

            for i in list_att:
                if i=='':
                    m = "check your information again, there seems to be an issue"
                    return render(request, 'application_for_job.html', {'message':m})
            appln = application(Full_Name = fname, Emailaddress=email, phone=phone, Address=address, Country=country, University_or_College=uoc, Year_of_study=yos, Transcript=myfile1, Sop=myfile2)
            appln.save()
            return redirect('success_appln')
    else:
        return redirect('login1')      
    return render(request, 'application_for_job.html')


def scholarships(request):
    return render(request, 'jobs.html')

def categories(request):
    return render(request, 'education.html')

def engineering(request):
    return render(request, 'engineering.html')

def medical(request):
    return render(request, 'medical.html')

def humanities(request):
    return render(request, 'humanities.html')

def management(request):
    return render(request, 'management.html')

def success_appln(request):
    return render(request, 'suc.html')
