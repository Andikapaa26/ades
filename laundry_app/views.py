from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *

@login_required(login_url='login')
def beranda(request):
    koordinats = Koordinat.objects.all()
    laundrys = Laundry.objects.all()
    data = {  
        'Title' : "UAS PBO",
        'koordinats' : koordinats,
        'laundrys' : laundrys,
    } 
    print(request.user)
    return render(request, 'beranda.html', data)

def regis(request):
    if request.user.is_authenticated:
        return redirect('/beranda')

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')

        data = {  
            'Title' : "UAS PBO",
            'form' : form
        }
        return render(request, "regis.html", data)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/beranda')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/beranda')
            else:
                messages.info(request, "Username or Password is INCORRECT!")
                return render(request, "login.html")

        data = {  
            'Title' : "UAS PBO",
        }
        return render(request, "login.html", data)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def add(request):
    if request.POST:
        form = FormKoordinat(request.POST)
        if form.is_valid():
            form.save()
            form = FormKoordinat()
            data = {
                'Title' : "UAS PBO",
                "form" : form,
                "pesan" : "Data telah ditambahkan!",
                }
            return render(request, 'add.html', data)
    else:
        form = FormKoordinat()
        data = {
            'Title' : "UAS PBO",
            "form" : form,
            }
        return render(request, 'add.html', data)

@login_required(login_url='login')
def add_laundry(request):
    if request.POST:
        form = FormLaundry(request.POST)
        if form.is_valid():
            form.save()
            form = FormLaundry()
            data = {
                'Title' : "UAS PBO",
                "form" : form,
                "pesan" : "Data telah ditambahkan!",
                }
            return render(request, 'add_laundry.html', data)
    else:
        form = FormLaundry()
        data = {
            'Title' : "UAS PBO",
            "form" : form,
            }
        return render(request, 'add.html', data)

@login_required(login_url='login')
def update(request, id_koordinat):
    koordinat = Koordinat.objects.get(id = id_koordinat)
    judul = "Update Data"
    template = "update.html"

    if request.POST:
        form = FormKoordinat(request.POST, instance=koordinat)
        if form.is_valid():
            form.save()
            pesan = "Data berhasil diupdate!"
            data = {
                'Title' : "UAS PBO",
                "pesan" : pesan,
                "form" : form,
                "koordinat" : koordinat,
            }
            return render(request, template, data)
    else:
        form = FormKoordinat(instance=koordinat)
        data = {
            'Title' : "UAS PBO",
            'Heading' : "Update Data",
            "form" : form,
            "koordinat" : koordinat,

        }
        return render(request, template, data)

@login_required(login_url='login')
def update_laundry(request, id_laundry):
    laundry = Laundry.objects.get(id = id_laundry)
    judul = "Update Data"
    template = "update_laundry.html"

    if request.POST:
        form = FormLaundry(request.POST, instance=laundry)
        if form.is_valid():
            form.save()
            pesan = "Data berhasil diupdate!"
            data = {
                'Title' : "UAS PBO",
                "pesan" : pesan,
                "form" : form,
                "laundry" : laundry,
            }
            return render(request, template, data)
    else:
        form = FormLaundry(instance=laundry)
        data = {
            'Title' : "UAS PBO",
            'Heading' : "Update Data",
            "form" : form,
            "laundry" : laundry,

        }
        return render(request, template, data)

@login_required(login_url='login')
def delete(request, id_koordinat):
    koordinat = Koordinat.objects.get(id = id_koordinat)
    koordinat.delete()

    return redirect("/beranda/")

@login_required(login_url='login')
def delete_laundry(request, id_laundry):
    laundry = Laundry.objects.get(id = id_laundry)
    laundry.delete()

    return redirect("/beranda/")

# Create your views here.

