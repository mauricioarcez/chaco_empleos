# Generated by Django 4.2.3 on 2023-07-26 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_usuario_dni_alter_usuario_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, default='usuarios/usuario_default.png', null=True, upload_to='usuarios'),
        ),
    ]