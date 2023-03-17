from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=450)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class FeatProduct(models.Model):
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    product_name = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=450, default="")
    product_price = models.IntegerField(default=0)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

# class DisProducts(models.Model):
#     id = models.AutoField(primary_key=True, unique=True)
#     category = models.CharField(max_length=50, default="")
#     subcategory = models.CharField(max_length=50, default="")
#     name = models.CharField(max_length=50, default="")
#     desc = models.CharField(max_length=250, default="")
#     price = models.IntegerField(default=0)
#     pub_date = models.DateField()
#     image = models.ImageField(upload_to="shop/images", default="")
#
#     def __str__(self):
#         return self.name

