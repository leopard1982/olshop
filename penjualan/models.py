from django.db import models
from api_rest.models import Produk
from django.contrib.auth.models import User

# Create your models here.


class shoppingCart(models.Model):
    username_cart = models.CharField(max_length=200, default=None)
    kode_produk = models.ForeignKey(
        Produk, on_delete=models.RESTRICT, null=False, blank=False)
    jumlah = models.PositiveIntegerField(default=0)
    harganya = models.PositiveIntegerField(default=0)
    total_harga = models.BigIntegerField(default=0)

    def __str__(self):
        return self.kode_produk


class wishlistCart(models.Model):
    username_wishlist = models.ForeignKey(
        User, verbose_name="Username", on_delete=models.RESTRICT)
    kode_produk_wishlist = models.ForeignKey(
        Produk, verbose_name="Kode Produk", on_delete=models.RESTRICT)

    def __str__(self):
        return self.kode_produk_whishlist

    class Meta:
        unique_together = ("username_wishlist", "kode_produk_wishlist")
