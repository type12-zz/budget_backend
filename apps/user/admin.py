from django.contrib import admin

# Register your models here.
from .models import User

admin.site.register(User)
class UserModel(admin.ModelAdmin):
    fields = ['name', 'email', 'profile', 'token', 'token_expires']
    list_filter = []
    list_display = fields
    search_fields = ['name', 'email']
