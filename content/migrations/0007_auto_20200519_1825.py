# Generated by Django 3.0.3 on 2020-05-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20200519_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(default='images/01-boxed.jpg', upload_to='images/'),
        ),
    ]