# Generated by Django 4.2.5 on 2023-11-26 21:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socios', '0002_user_dni_alter_user_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'verbose_name_plural': 'actividades',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.FloatField()),
                ('hasta', models.FloatField()),
                ('mensualidad', models.IntegerField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Dia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(max_length=9, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('fecha', models.DateField()),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.curso')),
            ],
            options={
                'verbose_name_plural': 'inscripciones',
            },
        ),
        migrations.CreateModel(
            name='DiaCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.curso')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socios.dia')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(through='socios.Inscripcion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='curso',
            name='dias',
            field=models.ManyToManyField(through='socios.DiaCurso', to='socios.dia'),
        ),
        migrations.AddField(
            model_name='curso',
            name='predio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='socios.predio'),
        ),
    ]
