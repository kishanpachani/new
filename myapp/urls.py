from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
   path('',views.index),
   path('about/',views.about),
   path('contact/',views.contact),
   path('products/',views.products,name='product'),
   path('cart/',views.cart_p,name='cart'),
   path('Userlogout/',views.Userlogout),
   path('addtocart/',views.addtocart,name='addtocart'),
 ]