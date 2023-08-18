from django.db import models
from api_rest.models import Produk

# Create your models here.
class shoppingCart(models.Model):
    username_cart = models.CharField(max_length=200,default=None)
    kode_produk = models.ForeignKey(Produk,on_delete=models.RESTRICT,null=False,blank=False)
    jumlah = models.PositiveIntegerField(default=0)