from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .forms import NewUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('user:profile')

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            login(request, user) # biz yaratgan userni login qiladi
            messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
            return redirect('user:login')
    return render(request, 'user/register.html', {'form': NewUserForm()})


def login_view(request):

    next = request.GET.get('next')

    print("-------------------------", next)

    if request.user.is_authenticated:
        return redirect('user:profile')

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
                messages.success(request, 'Tizimga muvoffaqiyatli kirdingiz!')
                return redirect(next)
    return render(request, 'user/login.html', {'form': AuthenticationForm()})

def profile(request):
    return render(request, 'user/profile.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Tizimdan chiqdingiz!')
    return redirect('user:login')