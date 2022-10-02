from django.shortcuts import render, redirect
from django.views import View
from .models import User
from hashlib import md5
from django.contrib import messages

# Create your views here.
class Home(View):
    template_name = 'home.html'
    def get(self, request):
        if 'user' not in request.session:
            return redirect('login')
        else:
            return render(request, self.template_name)

class RegisterView(View):
    template_name = 'register.html'
    def get(self, request):
        return render(request, self.template_name)
    def post(self, request):
        fname = request.POST['uname']
        pwd = request.POST['pwd']
        mail = request.POST['email']
        gender = request.POST['gender']
        # Hash the passwords
        unique_email = User.objects.filter(email=mail)
        
        if unique_email.exists():
            messages.warning(request, 'Email exists')
            return render(request, self.template_name)
        else:
            hash_pwd = md5(pwd.encode()).hexdigest()
            register_user = User.objects.create(fname=fname, password=hash_pwd, email=mail, gender=gender)
            register_user.save()
            messages.success(request, 'your account created successfully.')
            return redirect('login')
        


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        if 'user' in request.session:
            return redirect('home')
        else:
            return render(request, self.template_name)
    
    def post(self, request):
        mail = request.POST['email']
        pwd = request.POST['pwd']
        hash_pwd = md5(pwd.encode()).hexdigest()
        user_exists = User.objects.filter(email=mail, password=hash_pwd)
        if user_exists.exists():
            request.session['user'] = user_exists.first().fname
        else:
            messages.warning(request, 'Wrong credentials')
        return redirect('home')


class LogoutView(View):
    def get(self, request):
        del request.session['user']
        return redirect('login')
