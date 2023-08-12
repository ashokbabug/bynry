from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProblemType(models.Model):
    type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.type

class Problem(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    problem_type = models.ForeignKey(ProblemType,on_delete=models.CASCADE)   #Cascade is just for this assignment purpose
    problem_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True)
    attachment = models.FileField(upload_to='attachments',blank=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.problem_type} - {self.problem_description[0:10]}'