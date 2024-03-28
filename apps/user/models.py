from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class User(models.Model):
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    email = models.EmailField('Email', max_length=254, blank=False, null=False)
    password = models.CharField('Password', max_length=255, blank=False, null=False)
    budget = models.IntegerField('Budget', blank=False, null=False, default=0)
    token = models.CharField('Token', blank=True, null=True, max_length=500, db_index=True)
    profile = CloudinaryField("Profile Picture", blank=True, null=True)
    token_expires = models.DateTimeField('Token Expiration Date', blank=True, null=True)
    created_at = models.DateTimeField('Creation Date', blank=True, auto_now_add=True)
    updated_at = models.DateTimeField('Update Date', blank=True, auto_now=True)

    def __str__(self):
        return [self.name, self.email, self.password, self.budget]