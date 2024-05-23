from .models import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def view_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'authentication/user.html')
        return render(request, 'authentication/login.html', {'mensagem': 'Credenciais inválidas.','form':UserLoginForm(None)})
    return render(request, 'authentication/login.html', {'form':UserLoginForm(None)})

def view_register(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return render(request, 'authentication/register.html', {'mensagem':'Registo efetuado com sucesso', 'form':form})
    return render(request, 'authentication/register.html', {'form':form})

def view_logout(request):
    logout(request)
    return redirect('login')