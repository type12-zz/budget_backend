# Generated by Django 4.2.11 on 2024-03-27 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_rename_transactions_transaction'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
