from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user :
                login(request,user)
                messages.success(request, 'login successful!')
                return redirect('/')  
            messages.error(request,'login unsucessful! username and password does not match!Try again')  
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# def success(request):
#     return render(request, 'success.html')

def home(request):
    return render(request,'homepage.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email_address')
            form.save()
            sender="sapanaatamang123@gmail.com"
            receiver=[email]
            subject="account creation"
            body="account created successfully"
            send_mail(subject,body,sender,receiver)
            # password=password
            # user=form.save(commit=False)
            # # user.set_password(form.cleaned_data.get('pass'))
            
            return redirect('/login')  
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/login')



