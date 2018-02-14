from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress

# Create your models here.
class BucxMember(models.Model):
        member = models.OneToOneField(User,on_delete=models.CASCADE)
        u_name = models.CharField(max_length=30, blank=False)
        e_mail = models.OneToOneField(EmailAddress,on_delete=models.CASCADE)
        bio = models.TextField(max_length=500, blank=True)
        location = models.CharField(max_length=500, blank=True)
        birth_date = models.DateField(null=True, blank=True)
        joined = models.DateTimeField(auto_now=False, auto_now_add=True)
        lastvisited = models.DateTimeField(auto_now=True, auto_now_add=False)

        def __str__(self):
    		      return self.u_name
