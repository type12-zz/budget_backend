from django.contrib import admin

# Register your models here.
from .models import Category

admin.site.register(Category)
class CategoryModel(admin.ModelAdmin):
    fields = ['name', 'color_code']
    list_filter = []
    list_display = fields
    search_fields = ['name', 'color_code']