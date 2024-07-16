from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError

class Manager (BaseUserManager) : 
    def create_user(self, password, **fields) : 
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, **fields) : 
        fields.setdefault('is_staff', True)
        fields.setdefault('is_superuser', True)
        return self.create_user(**fields)
    

def validate_wa(val:str) :
    if not val.startswith('+2') : 
        raise ValidationError('must start with +2')
    
    if len(val) != 13 : 
        raise ValidationError('length must be 13')
    
    return val
    
class User (AbstractUser) : 
    objects = Manager()

    first_name = None
    last_name = None
    username = None
    
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=225)
    pharmcy_name = models.CharField(max_length=225)
    whats_app_number = models.CharField(max_length=20, validators=[validate_wa])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self) -> str:
        return self.full_name
    
