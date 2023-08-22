from django.db import models

# Create your models here.


class Signup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    Email=models.EmailField()
    password=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)

class add(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="image")
    price=models.BigIntegerField()
    

class cart(models.Model):
    userid = models.BigIntegerField()
    product_id = models.BigIntegerField()  
    contity = models.BigIntegerField()  
    created=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
    