# Generated by Django 3.2.3 on 2021-06-10 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('public_chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicchatroom',
            name='users',
            field=models.ManyToManyField(blank=True, help_text='users connected to chat', to=settings.AUTH_USER_MODEL),
        ),
    ]
