# Generated by Django 2.0.5 on 2018-05-21 07:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('messengerbot', '0002_auto_20180521_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirm_code',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]