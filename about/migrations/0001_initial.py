# Generated by Django 2.2.1 on 2019-07-21 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
                ('designation', models.TextField(max_length=100)),
                ('department', models.TextField(max_length=100)),
                ('university', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('cell', models.TextField(max_length=100)),
                ('image', models.FileField(upload_to='documents/')),
            ],
        ),
    ]