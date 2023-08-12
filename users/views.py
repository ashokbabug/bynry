from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)  #to get our information already filled in
        p_form = ProfileCreationForm(request.POST)#we are updating profile function
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            print(user)
            profile = p_form.cleaned_data
            profile = Profile(user=user,full_name=profile['full_name'],address=profile['address'],phone=profile['phone'])
            profile.save()
            messages.success(request, f'Your account has been created')
            return redirect('login')
    else:
       u_form = UserRegisterForm()
       p_form = ProfileCreationForm()
    context = {
    'u_form':u_form,
    'p_form':p_form
    }
    return render(request,'users/signup.html',context)