# Generated by Django 4.2.3 on 2023-08-17 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_produk_gambar1_produk_gambar2_produk_gambar3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produk',
            name='diskon_aktif',
            field=models.BooleanField(default=False, verbose_name='Setting Diskon Aktif/Tidak'),
        ),
        migrations.AddField(
            model_name='produk',
            name='produk_diskon',
            field=models.PositiveIntegerField(default=0, verbose_name='Diskon Produk (Rupiah)'),
        ),
        migrations.AddField(
            model_name='produk',
            name='produk_new',
            field=models.BooleanField(default=False, verbose_name='Setting Produk Sebagai New atau tidak'),
        ),
        migrations.AddField(
            model_name='produk',
            name='produk_rekomendasi',
            field=models.BooleanField(default=False, verbose_name='Setting Produk Rekomendasi atau tidak'),
        ),
        migrations.AddField(
            model_name='produk',
            name='terjual_asli',
            field=models.PositiveIntegerField(default=0, verbose_name='Jumlah Penjualan Otomatis Menghitung'),
        ),
        migrations.AddField(
            model_name='produk',
            name='terjual_fake',
            field=models.PositiveIntegerField(default=0, verbose_name='Jumlah Penjualan Untuk Menaikkan'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar1',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #1 (sebagai thumbnail)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar2',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #2 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar3',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #3 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar4',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #4 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar5',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #5 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar6',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #6 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar7',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #7 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='gambar8',
            field=models.ImageField(blank=True, null=True, upload_to='gbr_produk', verbose_name='Gambar #8 (optional)'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='produk_deskripsi',
            field=models.TextField(default='', max_length=1000, verbose_name='Deskripsi Produk'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='produk_harga',
            field=models.PositiveIntegerField(default=0, verbose_name='Harga Produk'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='produk_kode',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Kode Produk'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='produk_nama',
            field=models.CharField(default='', max_length=200, verbose_name='Nama Produk'),
        ),
    ]
