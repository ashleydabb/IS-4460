# Generated by Django 5.0.1 on 2024-03-03 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
