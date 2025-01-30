from django.shortcuts import render , redirect
from .models import user_register
from .models import user_login
from .forms import user_registerForm,user_loginForm
from django.contrib.auth import authenticate, login ,logout # must know
from django.contrib import messages  #must know
from django.contrib.auth.models import User   #must know

# Create your views here.

def cal(request):
    return render(request, 'posts/cal.html')





#def login(request):
    logs = user_login.objects.all()
    return render(request, 'posts/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['passwd']
        passwd2 = request.POST['password']

        if passwd == passwd2:
            try:
                user = User.objects.create_user(username=fname, email=email, password=passwd)
                user.save()
                user = authenticate(username=fname, password=passwd)
                login(request, user)
                return redirect('posts/login')
            except:
                error_message = 'Error creating account'
                return render(request, 'posts/register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'posts/register.html', {'error_message': error_message})
    return render(request, 'posts/register.html')

def login(request):
    if request.method == "POST":
        form1 = user_login(request.POST or None)
        if form1.is_valid():
            fname = form1.clean_fields['fname'] # request.POST
            passwd =form1.clean_fields['passwd'] # request.POST
            user = authenticate(username=fname, password=passwd)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('posts/cal')
            else:
                messages.error(request, 'Invalid username or password')
                #added you can remove
               
        else:
            messages.error(request, 'Invalid form data')
            #added you can remove
              # real login.html    return redirect('user_login')
    else:
        form1 = user_loginForm()
    return render(request, 'posts/login.html', {'form1': form1}) 