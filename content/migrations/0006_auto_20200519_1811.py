# Generated by Django 3.0.3 on 2020-05-19 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20200518_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.CharField(choices=[('Evet', 'Evet'), ('Hayır', 'Hayır')], default='Hayır', max_length=10),
        ),
    ]
