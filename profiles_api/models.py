from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password) # set password function automatically encrypts
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password): # we are overriding the existing function's definition
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True # apparently this is automatically created due to Mixin
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager() 
    # all models have at least one manager, 
    # which provides an api through which db queries are provided to the model
    # you can choose to extend or override it like the above
    # like adding custom query methods, or filtering or ordering results, etc.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name

    # specify how the model will look when you print it as a string
    def __str__(self):
        """Return string representation of our user"""
        return self.email
    
class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        # if user is deleted, 
        # then cascade and delete the profile feed item too
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text