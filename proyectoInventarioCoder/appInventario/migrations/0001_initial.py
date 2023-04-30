# Generated by Django 4.2 on 2023-04-30 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tablCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categNombre', models.CharField(max_length=100)),
                ('categDescrip', models.CharField(max_length=300)),
                ('categActivo', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tablMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marcaNombre', models.CharField(max_length=100)),
                ('marcaActiva', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='tablSubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategNombre', models.CharField(max_length=100)),
                ('subCategDescrip', models.TextField()),
                ('subCategActivo', models.CharField(max_length=2)),
                ('subCategCateg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appInventario.tablcategoria')),
            ],
        ),
        migrations.CreateModel(
            name='tablModelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modeloNombre', models.CharField(max_length=100)),
                ('modeloActivo', models.CharField(max_length=2)),
                ('modeloMarca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appInventario.tablmarca')),
            ],
        ),
    ]
