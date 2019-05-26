from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,ProfileForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})




def profile(request):
    if request.method=="GET":
        form = ProfileForm(instance=request.user.profile);
        return render(request,'users/profile.html',{'form':form});
    elif request.method=="POST":
        form = ProfileForm(request.POST,instance=request.user.profile);
        if form.is_valid():
            user = form.cleaned_data['user']
            if (request.user == user):
                form.save();
            else:
                return HttpResponse("user is not logged in")
            messages.success(request, f'{user} your profile is complete.')
        return redirect('home')