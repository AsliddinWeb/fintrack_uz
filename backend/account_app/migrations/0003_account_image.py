# Generated by Django 5.0.6 on 2024-05-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0002_alter_account_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='accounts/', verbose_name='Avatar'),
        ),
    ]