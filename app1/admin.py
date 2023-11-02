from django.contrib import admin
from .models import *
# Register your models here.

class blog_(admin.ModelAdmin):
    list_display = ['id','name','tagline']
    list_filter = ['name']
    search_fields = ['name','tagline']

admin.site.register(Blog1,blog_)
class cat_(admin.ModelAdmin):
    list_display = ['id','cat_name','image']
admin.site.register(Categ,cat_)

class User_(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','address','password','image']
admin.site.register(Userregister,User_)

class Product_(admin.ModelAdmin):
    list_display = ['id','Product_categ','Product_name','Product_price','Product_brand','Product_quntity','Product_image','Product_disc']
    list_filter = ['Product_name','Product_categ']
admin.site.register(Product,Product_)

class Wander_(admin.ModelAdmin):
    list_display = ['id','name','email','mobile','address','password','image']
admin.site.register(wandersignup,Wander_)

class Addcart_(admin.ModelAdmin):
    list_display = ['id','orderid','productid','userid','quntity','price','tprice']
admin.site.register(Addcart,Addcart_)