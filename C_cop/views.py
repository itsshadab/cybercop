from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html', {"name" : "Cyber Cop"})

def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f'Account is Created {first_name}!')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'pages/register.html', {"name" : "Cyber Cop", "form" : form})

@login_required
def urlshistory(request):
    return render(request, 'pages/urlshistory.html', {"name" : "Cyber Cop"})

def onclick(request):
    if request.GET.get('sort-btn'):
        cits = Citizen.objects.all().order_by('name')
    return render_to_response(request, 'civil_reg/index.html', {'cits': cits})