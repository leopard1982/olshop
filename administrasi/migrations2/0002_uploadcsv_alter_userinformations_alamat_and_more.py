# Generated by Django 4.2.3 on 2023-08-17 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadCSV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filenya', models.FileField(upload_to='csv_file', verbose_name='File CSV')),
            ],
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='alamat',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Alamat Lengkap'),
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='kecamatan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kecamatan', verbose_name='Pilihan Kecamatan'),
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='kota',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.kota', verbose_name='Pilihan Kota/ Kabupaten'),
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='nomor_hp',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Nomor HP (whatsapp)'),
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='propinsi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='administrasi.propinsi', verbose_name='Pilihan Propinsi'),
        ),
        migrations.AlterField(
            model_name='userinformations',
            name='user_id',
            field=models.CharField(default='', max_length=200, primary_key=True, serialize=False, verbose_name='User Name'),
        ),
    ]
