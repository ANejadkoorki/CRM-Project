# Generated by Django 3.2.5 on 2021-08-04 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellProcess', '0002_quote_expert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quoteitem',
            name='price',
        ),
    ]
