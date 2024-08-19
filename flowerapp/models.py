from django.db import models


# Create your models here.

class Flower(models.Model):
    flower_id = models.AutoField(primary_key=True)
    flower_name = models.CharField(max_length=200)
    flower_price = models.IntegerField()
    flower_description = models.TextField()
    flower_image = models.ImageField(upload_to='')

    class Meta:
        db_table = 'flower_table'


class AddCart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)



class BuyNow(models.Model):
    buy_id = models.AutoField(primary_key=True)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=255)
    razorpay_id = models.CharField(max_length=255)
    paid = models.BooleanField(default=False)



class UserRegister(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200, default=1)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    address = models.CharField(max_length=255, default=1)
    password = models.CharField(max_length=12)
    image = models.ImageField(upload_to='', default='person.jpg')


class PanUser(models.Model):
    pan_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pan_number = models.CharField(max_length=50)
    pan_image = models.ImageField(upload_to='')

    class Meta:
        db_table = 'panuser_table'
