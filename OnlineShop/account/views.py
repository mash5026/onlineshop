from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import UserLoginForm, UserRegistrationForm, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, mobile=cd['mobile'], password=cd['password'])
            if user is not  None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'account/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, 'you logged out successfully', 'success')
    return redirect('shop:home')


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['email'], cd['mobile'], cd['address'], cd['full_name'], cd['password'])
            user.save()
            messages.success(request, 'your registration successful.', 'success')
            return redirect('shop:home')

    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)


@login_required
def edit_profile(request):
    if request.method != 'POST':
        form = EditProfile(instance=request.user)
    else:
        form = EditProfile(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'کاربری شما به روز گردید.')
    context = {
        'form': form,
    }
    return render(request, 'account/edit.html', context)

