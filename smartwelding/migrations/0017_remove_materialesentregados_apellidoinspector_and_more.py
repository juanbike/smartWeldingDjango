# Generated by Django 4.2 on 2023-06-13 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smartwelding', '0016_remove_soldador_altura_remove_soldador_edad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materialesentregados',
            name='apellidoInspector',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='apellidoSoldador',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='coladaE',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='materialE',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='nombreInspector',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='nombreProyecto',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='nombreSoldador',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='sheduleE',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='tipoE',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='tipoExtremoE',
        ),
        migrations.RemoveField(
            model_name='materialesentregados',
            name='tipoMaterialE',
        ),
        migrations.AddField(
            model_name='materialesentregados',
            name='inspector',
            field=models.ForeignKey(default='Inspector', on_delete=django.db.models.deletion.CASCADE, to='smartwelding.inspector'),
        ),
        migrations.AddField(
            model_name='materialesentregados',
            name='material',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='smartwelding.materiales'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materialesentregados',
            name='proyecto',
            field=models.ForeignKey(default='Proyecto', on_delete=django.db.models.deletion.CASCADE, to='smartwelding.proyecto'),
        ),
        migrations.AddField(
            model_name='materialesentregados',
            name='soldador',
            field=models.ForeignKey(default='Soldador', on_delete=django.db.models.deletion.CASCADE, to='smartwelding.soldador'),
        ),
    ]
