# Generated by Django 2.2.1 on 2019-07-22 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='about',
            name='department',
        ),
        migrations.RemoveField(
            model_name='about',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
        migrations.RemoveField(
            model_name='about',
            name='university',
        ),
    ]
