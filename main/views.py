from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import appl_info_form

# Create your views here.

def home(request):
    return render(request, 'home.html')

def appl_info(request):
    if request.method == 'POST':
        form = appl_info_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_appln')
    else:
        form = appl_info_form()
    return render(request, 'appl_info.html', {'form': form})


def success_appln(request):
    return HttpResponse("SUCCESSFULLY APPLIED !!!! :)))")
