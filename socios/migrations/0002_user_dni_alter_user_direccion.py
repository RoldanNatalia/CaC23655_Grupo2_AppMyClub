# Generated by Django 4.2.5 on 2023-11-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dni',
            field=models.CharField(default='11111111', max_length=8),
        ),
        migrations.AlterField(
            model_name='user',
            name='direccion',
            field=models.CharField(default='n/a', max_length=100),
        ),
    ]
