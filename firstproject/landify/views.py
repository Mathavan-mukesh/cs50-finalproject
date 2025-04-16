from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserResponseForm,ContactForm
from .models import UserResponse


def hello_world(request):
    return HttpResponse("Hello, World!")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()

    return render(request, 'landify/register.html', {'form': form})  

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('news') 
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'landify/login.html')

def seller(request):
    if request.method == 'POST':
        form = UserResponseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news')
    else:
        form = UserResponseForm()
    return render(request, 'landify/seller.html', {'form': form})

def nav(request):
    return render(request, "includes/nav.html")

def footer(request):
    return render (request, "includes/footer.html")

def policy(request):
    return render (request, "landify/policy.html")

def terms(request):
    return render (request, "landify/terms.html")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, "Thank you! Your message has been sent.")
            return redirect('contact')  
        else:
            messages.error(request, "There was an error. Please try again.")
    else:
        form = ContactForm()

    return render(request, 'landify/contact.html', {'form': form})

def base(request):
    return render(request, "landify/base.html")

def services(request):
    return render(request, "landify/services.html")

def about(request):
    return render(request, "landify/about.html")

def news_view(request):
    user_responses = UserResponse.objects.all()
    
    return render(request, 'landify/news.html', {'user_responses': user_responses})