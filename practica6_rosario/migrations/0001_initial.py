# Generated by Django 5.0.2 on 2024-03-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('significado', models.CharField(max_length=30)),
                ('tamaño', models.CharField(choices=[('Pequeña', 'Pequeña'), ('Mediana', 'Mediana'), ('Grande', 'Grande')], max_length=30)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]