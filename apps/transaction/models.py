from django.db import models
from apps.category.models import Category
from apps.user.models import User
from backend.constants import *
from django.core.validators import MinValueValidator

# Create your models here.
class Transaction(models.Model):
    name = models.CharField(blank=False, null=False, max_length=200)
    user = models.ForeignKey(User, related_name='related_user', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='related_category', on_delete=models.CASCADE)
    type = models.CharField(blank=False, null=False, max_length=50)
    amount = models.IntegerField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, auto_now=True)