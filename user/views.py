from django.shortcuts import redirect, render
from .forms import RegiserForm, UpdateUser
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
# Create your views here.


def signup(request):
    message = ''
    if request.method == 'POST':
        form = RegiserForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('userapp:home')
        else:
            print(request.POST)
            message = 'Information Incorrect or Already Exists'
    context = {'message': message}
    return render(request, 'registration/sign_up.html', context)


def userprofile(request, username):
    print(username)
    user = User.objects.filter(username=username).first()
    form = UpdateUser(instance=User)
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user/user_informations.html')
