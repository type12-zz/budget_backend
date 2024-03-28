from django.db import models

# Create your models here.
class Category(models.Model):
    class Meta(object):
        db_table = 'category'
        verbose_name_plural = "Categories"
        
    name = models.CharField(max_length=50, blank=False, null=False)
    color_code = models.CharField('Color Code', blank=False, null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name