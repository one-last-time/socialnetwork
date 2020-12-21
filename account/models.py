from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username,first_name,last_name,password,**other_fields):
        if not email:
            raise ValueError('User must have valid email')
        if not username:
            raise ValueError('Username cant be emoty')
        if not first_name:
            raise ValueError('First name cant be empty')
        if not last_name:
            raise ValueError('Last name cant be empty')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self, email, username,first_name,last_name, password,**other_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_stuff = True
        


class Account(AbstractBaseUser):
    email =  models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(verbose_name = 'username', max_length=30)
    first_name = models.CharField(verbose_name = 'first_name', max_length=30)
    last_name = models.CharField(verbose_name = 'last_name', max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_active = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','email','first_name','last_name']
    
    def __str__(self):
        return self.email+" "+self.username
    
    def has_perm(self, prem, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True 
    
    
