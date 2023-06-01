# Generated by Django 4.1.6 on 2023-06-01 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrador',
            fields=[
                ('id_administrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='c_tipo_platillo',
            fields=[
                ('id_tipo_platillo', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='c_ubicacion',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='tableta',
            fields=[
                ('id_tableta', models.AutoField(primary_key=True, serialize=False)),
                ('numero_mesa', models.IntegerField(default=0)),
                ('ubicacion', models.CharField(max_length=50)),
                ('id_ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.c_ubicacion')),
            ],
        ),
        migrations.CreateModel(
            name='platillo',
            fields=[
                ('id_platillo', models.AutoField(primary_key=True, serialize=False)),
                ('descrpcion', models.CharField(max_length=300)),
                ('precio', models.CharField(max_length=50)),
                ('imagen', models.TextField()),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.administrador')),
                ('id_tipo_platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.c_tipo_platillo')),
            ],
        ),
        migrations.CreateModel(
            name='orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('numero_mesa', models.IntegerField(default=0)),
                ('id_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.administrador')),
                ('id_platillos', models.ManyToManyField(to='FiftyFriends.platillo')),
                ('id_tableta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.tableta')),
                ('id_tipo_platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.c_tipo_platillo')),
                ('id_ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FiftyFriends.c_ubicacion')),
            ],
        ),
    ]
