# Generated by Django 3.2.18 on 2023-05-10 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0009_auto_20230510_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='expense_account',
        ),
    ]
