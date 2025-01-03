# Generated by Django 4.2.9 on 2024-01-24 03:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id_elemento', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('cantidad', models.IntegerField()),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('U', 'Unisex')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tallas', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='elementos/')),
                ('imagen_dos', models.ImageField(blank=True, null=True, upload_to='elementos/')),
                ('imagen_tres', models.ImageField(blank=True, null=True, upload_to='elementos/')),
                ('coleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='elementos', to='tienda_ropa.coleccion')),
            ],
        ),
    ]
