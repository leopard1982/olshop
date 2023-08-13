from django.db import models

# Create your models here.
class Produk(models.Model):
    produk_kode = models.CharField(max_length=200,primary_key=True,blank=False,null=False)
    produk_nama = models.CharField(max_length=200,blank=False,null=False,default="")
    produk_harga = models.PositiveIntegerField(default=0,blank=False,null=False)
    produk_deskripsi = models.TextField(max_length=1000,blank=False,null=False,default="")
    gambar1 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar2 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar3 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar4 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar5 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar6 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar7 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)
    gambar8 = models.ImageField(upload_to="gbr_produk",blank=True,null=True)