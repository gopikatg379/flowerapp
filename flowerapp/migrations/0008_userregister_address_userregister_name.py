# Generated by Django 5.1 on 2024-08-19 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowerapp', '0007_userregister_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregister',
            name='address',
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name='userregister',
            name='name',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
