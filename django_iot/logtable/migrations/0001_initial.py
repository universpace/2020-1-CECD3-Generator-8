# Generated by Django 2.2.13 on 2020-08-06 02:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=15)),
                ('levels', models.IntegerField()),
            ],
            options={
                'ordering': ['building_name'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_num', models.IntegerField()),
                ('img_file_path', models.CharField(max_length=200)),
                ('building_id', models.ForeignKey(default=uuid.uuid4,
                                                  on_delete=django.db.models.deletion.CASCADE, to='logtable.Building')),
            ],
            options={
                'ordering': ['level_num'],
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_code', models.CharField(default='DGU', max_length=10, unique=True)),
                ('sensor_name', models.CharField(db_index=True, max_length=10, null=True)),
                ('sensor_type', models.CharField(choices=[('IG', 'Intergration'), ('RD', 'Radar'), ('RF', 'RF')], max_length=2)),
                ('sensor_status', models.CharField(choices=[('OP', 'Operational'), ('TE', 'Temporary Error'), ('BR', 'Broken'), ('ND', 'Not Defined')], default='ND', max_length=2)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logtable.Level')),
            ],
            options={
                'ordering': ['sensor_code'],
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sensor', to='logtable.Sensor')),
            ],
        ),
    ]
