# Generated by Django 2.2.1 on 2019-06-28 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_remove_quote_quote_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuoteCategory',
        ),
    ]
