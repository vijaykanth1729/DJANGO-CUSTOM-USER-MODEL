from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistrationForm
from .models import RegisterUser, CustomUser
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
                return HttpResponse("<h1>Login Success</h1>")
            else:
                messages.warning(request, 'Improper credntails')
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # phone_number = request.POST.get('phone_number')
        if form.is_valid():
            # user = CustomUser.objects.create_user(email=email,password=password,phone_number=phone_number)
            # user.save()
            form.save()
            # #user = RegisterUser.objects.create_user()
            # form.save(commit=True)
            return HttpResponse("Registration success")
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})
