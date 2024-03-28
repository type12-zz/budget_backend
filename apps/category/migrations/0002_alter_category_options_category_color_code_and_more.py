# Generated by Django 4.2.11 on 2024-03-28 00:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='color_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Color Code'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]