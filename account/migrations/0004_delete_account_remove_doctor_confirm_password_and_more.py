# Generated by Django 4.2 on 2023-05-23 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_account_email_remove_account_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='confirm_password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
    ]
