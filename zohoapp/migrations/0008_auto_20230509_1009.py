# Generated by Django 3.2.18 on 2023-05-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0007_expense_sac'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='taxamt',
            field=models.TextField(default=100, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='reporting_tags',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
