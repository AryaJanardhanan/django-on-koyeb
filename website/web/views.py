from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout

# Create your views here.
def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'home.html', {'username': username})

def indextem(request):
    return render(request,'indextem.html')

def contact(request):
    return render(request,'contact.html')
#CRUD OPERATIONS
#dat = Library.objects.all()   #all objects
#dat1 = Library.objects.get(pk=1)    #single object
##dat2 = Library.objects.filter(name = 'value')   #objects with condition
#dat3 = Library.objects.filter(name = 'value').first()  

#create new object
#obj = Library(name='value', auth='value')
#obj.save()

#update
#obj = Book()
#obj.field1 = 'new value'
#obj.save()

#obj.delete()



def about(request):
    return redirect('about.html')


@login_required
def success(request):
    return render(request, 'success.html')



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save the user object
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)  
            user.save() 

            # Save the profile object
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            profile = Profile.objects.create(user=user, first_name=first_name, last_name=last_name,username=username)
            return redirect('uslogin') 
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def uslogin(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def uslogout(request):
    logout(request)
    return redirect('home')


def list(request):
    items = Item.objects.all()
    return render(request, 'itemlist.html', {'items': items})


def editt(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemsForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ItemsForm(instance=item)
    return render(request, 'edit.html', {'form': form})


def delte(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list')
    return render(request, 'cnfrm.html', {'item': item})


def add(request):
    if request.method == 'POST':
        form = ItemsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = ItemsForm()
    return render(request, 'add.html', {'form': form})


def upload(request):
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = ImageUpload()
    return render(request, 'upload.html', {'form': form})

