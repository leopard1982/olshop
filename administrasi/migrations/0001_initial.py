# Generated by Django 4.2.3 on 2023-08-17 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('kode_kecamatan', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_kecamatan', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('kode_kota', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_kota', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Propinsi',
            fields=[
                ('kode_propinsi', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_propinsi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserInformations',
            fields=[
                ('user_id', models.CharField(default='', max_length=200, primary_key=True, serialize=False)),
                ('nomor_hp', models.CharField(blank=True, max_length=20, null=True)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
                ('point', models.IntegerField(default=0)),
                ('kecamatan', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kecamatan')),
                ('kota', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kota')),
                ('propinsi', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.propinsi')),
            ],
        ),
        migrations.AddField(
            model_name='kota',
            name='kode_propinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.propinsi'),
        ),
        migrations.AddField(
            model_name='kecamatan',
            name='kode_kota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kota'),
        ),
    ]
