from django.db import models

# Create your models here.
class Blog1(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name 
class Categ(models.Model):
    cat_name = models.CharField(max_length=50)
    image =  models.ImageField(upload_to='cat_img')
    def __str__(self):
        return self.cat_name 
    
class Userregister(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)
    address = models.TextField(default=" ")
    image = models.ImageField(upload_to='cat',default=" ")
     
    def __str__(self):
        return self.name
    
class Product(models.Model):
    Product_categ = models.ForeignKey(Categ, on_delete=models.CASCADE)
    Product_name = models.CharField(max_length=50)
    Product_price = models.IntegerField()
    Product_brand = models.CharField(max_length=50)
    Product_quntity = models.CharField(max_length=50)
    Product_image = models.ImageField(upload_to='product_image')
    Product_disc = models.CharField(max_length=50)

class wandersignup(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)
    address = models.TextField(max_length=50)
    image = models.ImageField(upload_to='wander')
     
    def __str__(self):
        return self.name
    
class Addcart(models.Model):
    orderid = models.CharField(max_length=50)
    productid = models.CharField(max_length=50)
    userid = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    tprice = models.CharField(max_length=50)
    quntity = models.CharField(max_length=50,default=" ")
    def __str__(self):
        return self.orderid
    