from django.db import models
import datetime
import os
from django.contrib.auth.models import User


# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Category(models.Model):
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    img = models.ImageField(upload_to='store/data', height_field=None, width_field=None, max_length=None)
    desc = models.TextField(max_length=500, default="")
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    meta_title = models.CharField(max_length=150, default="")
    meta_keywords = models.CharField(max_length=150, default="")
    meta_desc = models.TextField(max_length=500, default="")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    p_img = models.ImageField(upload_to='store/data', height_field=None, width_field=None, max_length=None)
    s_desc = models.CharField(max_length=120, default="")
    desc = models.TextField(max_length=500, default="")
    quantity = models.IntegerField()
    price = models.FloatField()
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    tag = models.CharField(max_length=50)
    meta_title = models.CharField(max_length=150, default="")
    meta_keywords = models.CharField(max_length=150, default="")
    meta_desc = models.TextField(max_length=500, default="")
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)


class Wish_List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)

    total_price = models.FloatField(null=False)
    payment_mode = models.CharField(max_length=100, null=False)
    payment_id = models.CharField(max_length=30, null=True)

    orderstatus = (
        ("pending", "pending"),
        ("out for shipping", "out for shipping"),
        ("completed", "completed")
    )
    status = models.CharField(max_length=200, choices=orderstatus, default="pending")

    message = models.TextField(null=True)
    tracking_num = models.CharField(max_length=100, null=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.tracking_num)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.order.id, self.order.tracking_num)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    state = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


