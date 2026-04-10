from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import resend
from django.conf import settings
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login, authenticate, logout

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username,
            password=password)
        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send(
            {
              'from':'onboarding@resend.dev',
                'to': ['kdb6208@gmail.com'],  
                'subject': 'Welcome to Medha HMS',
                'html': f'<h1>Welcome {user.username}</h1>'
            }
        )
        auth_login(request, user)
        return redirect('dashboard')
    else:
        return render(request, 'user_signup.html')
    


    
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'user_login.html')

def user_logout(request):
         logout(request)
         return redirect('home')
