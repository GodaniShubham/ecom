from django.urls import path
from .views import *
urlpatterns = [
    # path('',index,name="index"),
    # path('',register,name="register"),
    path('register/',register,name="register"),
    path('home/',home,name="home"),
    path('login/',login,name="login"),
    # path('private/',private,name="private"),
    path('logout/',logout,name="logout"),
    path('user/',user,name="user"),
    path('',main,name="main"),  
    path('product/<int:id>',product,name='product'),
    path('Productdetail/<int:id>',product_details,name='product_details'),
    path('wandersignup/',Wandersignup,name="wandersignup"),
    path('wanderlogin/',wanderlogin,name="wanderlogin"),
    path('wanderlogout/',wanderlogout,name="wanderlogout"),
    path('addproduct/',addproduct,name="addproduct"),
    path('addcategory/',addcate,name="addcate"),
    path('Cart/',cart,name="cart"),
    path('pluspro/<int:id>',pluspro,name="pluspro"),
    path('subpro/<int:id>',subpro,name="subpro"),
    path('remove/<int:id>',remove,name="remove"),
    path('removeall/',removeall,name="removeall"),

]