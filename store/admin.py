from django.contrib import admin

# Register your models here.
from .models import Product, Cart, CartItem, Order, OrderItem

admin.site.register(Product)

class CartItemInline(admin.TabularInline):
    model = CartItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]

# admin.site.register(Product): 註冊Product模型以便在Django管理後臺中管理商品

# CartItemInline類: 創建一個內連類，用於在Cart管理頁面中直接編輯CartItem

# CartAdmin類: 註冊Cart模型，並指定CartItemInline作為內連，這樣在Cart管理頁面中直接編輯CartItem

# OrderItemInline類: 創建一個內連類，用於在Order管理頁面中直接編輯OrderItem

# OrderAdmin類: 註冊Order模型，並指定OrderItemInline作為內連，這樣在Order管理頁面中直接編輯OrderItem