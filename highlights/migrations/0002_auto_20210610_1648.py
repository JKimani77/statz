# Generated by Django 3.2.3 on 2021-06-10 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('highlights', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.DeleteModel(
            name='Peopletoo',
        ),
    ]
