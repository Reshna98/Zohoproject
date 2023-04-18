# Generated by Django 4.2 on 2023-04-18 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0023_additem_history_delete_producthistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additem',
            old_name='history',
            new_name='creat',
        ),
        migrations.AddField(
            model_name='history',
            name='p',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem'),
            preserve_default=False,
        ),
    ]