from django.db import models

# Create your models here.
class Produk(models.Model):
    produk_kode = models.CharField(max_length=200,primary_key=True,blank=False,null=False,verbose_name="Kode Produk")
    produk_nama = models.CharField(max_length=200,blank=False,null=False,default="",verbose_name="Nama Produk")
    produk_deskripsi = models.TextField(max_length=1000,blank=False,null=False,default="",verbose_name="Deskripsi Produk")
    produk_harga = models.PositiveIntegerField(default=0,blank=False,null=False,verbose_name="Harga Produk")
    produk_diskon = models.PositiveIntegerField(default=0,blank=False,null=False,verbose_name="Diskon Produk (Rupiah)")
    diskon_aktif = models.BooleanField(default=False,verbose_name="Setting Diskon Aktif/Tidak")
    gambar1 = models.ImageField(upload_to="gbr_produk",blank=True,null=True, verbose_name="Gambar #1 (sebagai thumbnail)")
    gambar2 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #2 (optional)")
    gambar3 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #3 (optional)")
    gambar4 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #4 (optional)")
    gambar5 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #5 (optional)")
    gambar6 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #6 (optional)")
    gambar7 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #7 (optional)")
    gambar8 = models.ImageField(upload_to="gbr_produk",blank=True,null=True,verbose_name="Gambar #8 (optional)")
    terjual_asli = models.PositiveIntegerField(default=0,verbose_name="Jumlah Penjualan Otomatis Menghitung")
    terjual_fake = models.PositiveIntegerField(default=0,verbose_name="Jumlah Penjualan Untuk Menaikkan")
    produk_new = models.BooleanField(default=False,verbose_name="Setting Produk Sebagai New atau tidak")
    produk_rekomendasi = models.BooleanField(default=False,verbose_name="Setting Produk Rekomendasi atau tidak")