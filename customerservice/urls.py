from django.urls import path,include
from .views import *

urlpatterns = [
    path('',addproblem,name='add-complaint'),
    path('get-all-problems/',getAllProblems,name='all-complaints')
]