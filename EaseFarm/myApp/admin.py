from django.contrib import admin
from myApp.models import Contact, Customer, Product, Cart, OrderPlaced


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'desc', 'date']


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'aadhar_card_no', 'email', 'phone_no', 'another_phone_no', 'time', 'locality', 'city', 'state',
                    'zipcode']


@admin.register(Product)
class ProductUser(admin.ModelAdmin):
    list_display = ['id', 'name_of_owner', 'phone_no', 'title', 'rent_price', 'brand', 'description',
                    'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'time', 'product', 'quantity']


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'time', 'ordered_date', 'status']

from .models import Contact, Customer, Product, Cart, OrderPlaced