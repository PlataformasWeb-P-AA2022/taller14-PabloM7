# Generated by Django 4.0.5 on 2022-07-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propietario',
            name='nacionalidad',
            field=models.CharField(choices=[('ecuatoriana', 'Ecuatoriana'), ('peruana', 'Peruana'), ('colombiana', 'Colombiana')], max_length=30),
        ),
    ]
