# Generated by Django 4.2.5 on 2023-10-03 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_persona_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='direccion',
            field=models.CharField(default='ingrese una direccion..', max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(max_length=60),
        ),
    ]
