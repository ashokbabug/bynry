from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=255,null=False)
    phone = models.BigIntegerField(null=False)
    def __str__(self):
        return f'{self.user.username} profile'

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         # print("create",sender, instance,created,**kwargs)
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     # print("save",sender, instance,**kwargs)
    #     instance.profile.save()

    

	
