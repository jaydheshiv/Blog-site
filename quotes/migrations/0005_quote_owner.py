# Generated by Django 3.0.3 on 2020-02-20 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_quote_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='owner',
            field=models.CharField(max_length=50, null=True),
        ),
    ]