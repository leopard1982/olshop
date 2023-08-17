from django.db import models

class Propinsi(models.Model):
    kode_propinsi = models.CharField(max_length=10,primary_key=True,null=False,blank=False)
    nama_propinsi = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_propinsi

class Kota(models.Model):
    kode_propinsi = models.ForeignKey(Propinsi, on_delete=models.RESTRICT,blank=False,null=False)
    kode_kota = models.CharField(max_length=10,primary_key=True,blank=False,null=False)
    nama_kota = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_kota

class Kecamatan(models.Model):
    kode_kota = models.ForeignKey(Kota, on_delete=models.RESTRICT,blank=False,null=False)
    kode_kecamatan = models.CharField(max_length=10,primary_key=True,blank=False,null=False)
    nama_kecamatan = models.CharField(max_length=200)

    def __str__(self):
        return self.nama_kecamatan

# Create your models here.
class UserInformations(models.Model):
    user_id = models.CharField(max_length=200,primary_key=True,blank=False,null=False,default="",verbose_name="User Name")
    nomor_hp = models.CharField(max_length=20,blank=True,null=True,verbose_name="Nomor HP (whatsapp)")
    alamat = models.CharField(max_length=200,blank=True,null=True,verbose_name="Alamat Lengkap")
    propinsi = models.ForeignKey(Propinsi,on_delete=models.RESTRICT,verbose_name="Pilihan Propinsi")
    kota = models.ForeignKey(Kota,on_delete=models.RESTRICT,verbose_name="Pilihan Kota/ Kabupaten")
    kecamatan = models.ForeignKey(Kecamatan,on_delete=models.RESTRICT,verbose_name="Pilihan Kecamatan")
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.user_id

class uploadCSV(models.Model):
    filenya = models.FileField(upload_to="csv_file",verbose_name="File CSV")
