# Generated by Django 5.0.6 on 2024-05-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0002_alter_expense_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensecategory',
            name='icon',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Kategoriya rasmi'),
        ),
    ]
