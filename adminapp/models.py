from django.db import models


# Create your models here.

class Register_user(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_email = models.CharField(max_length=255)
    user_pwd = models.CharField(max_length=20)

    class Meta:
        db_table = 'register_user'
