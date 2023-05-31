# Generated by Django 4.2 on 2023-05-31 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartwelding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('contacto', models.CharField(max_length=80)),
                ('creado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Soldadores',
            new_name='Soldador',
        ),
    ]