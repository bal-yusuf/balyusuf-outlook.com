# Generated by Django 3.0.3 on 2020-05-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20200519_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
