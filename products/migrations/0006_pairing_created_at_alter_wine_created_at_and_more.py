# Generated by Django 5.1.4 on 2025-01-07 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_cheese_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='pairing',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='wine',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
