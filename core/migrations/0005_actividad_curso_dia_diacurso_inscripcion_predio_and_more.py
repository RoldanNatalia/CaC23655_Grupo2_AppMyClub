# Generated by Django 4.2.5 on 2023-10-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_persona_email_alter_persona_direccion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desde', models.FloatField()),
                ('hasta', models.FloatField()),
                ('mensualidad', models.IntegerField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.actividad')),
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
            name='DiaCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.dia')),
            ],
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
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
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=8)),
                ('email', models.EmailField(default='to1@example.com', max_length=100)),
                ('direccion', models.CharField(default='Domicilio..', max_length=100)),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.actividad')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=8)),
                ('email', models.EmailField(default='to1@example.com', max_length=100)),
                ('direccion', models.CharField(default='Domicilio..', max_length=100)),
                ('numero', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.socio'),
        ),
        migrations.AddField(
            model_name='inscripcion',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='alumnos',
            field=models.ManyToManyField(through='core.Inscripcion', to='core.socio'),
        ),
        migrations.AddField(
            model_name='curso',
            name='dias',
            field=models.ManyToManyField(through='core.DiaCurso', to='core.dia'),
        ),
        migrations.AddField(
            model_name='curso',
            name='predio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.predio'),
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.profesor'),
        ),
    ]
