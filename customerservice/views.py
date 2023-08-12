from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def addproblem(request):
    
    if request.method=='POST':
        form = ProblemCreationForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user=request.user
            problem.save()
            messages.success(request, f'Complaint registed successfully')
            return redirect('/get-all-problems')	    

	
    else:

        form = ProblemCreationForm()

    return render(request,'gas/problemcreationform.html',{'form':form})



@login_required
def getAllProblems(request):
    problems = Problem.objects.filter(user=request.user).order_by('-created_at')
    context = {'problems':problems,'username':request.user.username}
    return render(request,'gas/problems.html',context)
     
