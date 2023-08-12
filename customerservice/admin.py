from django.contrib import admin
from .models import *
# Register your models here.

class ProblemAdmin(admin.ModelAdmin):
    list_display = ['user','problem_type','created_at','resolved_at','resolved',]
    list_filter = ['resolved']
    list_per_page = 25
    search_fields = ('problem_type','problem_description')
admin.site.register(Problem,ProblemAdmin)
admin.site.register(ProblemType)

