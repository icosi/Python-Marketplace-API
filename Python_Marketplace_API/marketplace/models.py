# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CartProductRelation(models.Model):
    relation_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey('Carts', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_product_relation'


class Carts(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'carts'


class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, blank=True, null=True)
    category = models.CharField(max_length=36, blank=True, null=True)
    description = models.CharField(max_length=36, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36, blank=True, null=True)
    last_name = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
