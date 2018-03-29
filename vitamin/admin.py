from django.contrib import admin

from .models import Vitamin, Product, VitaminInProduct


@admin.register(Vitamin)
class VitaminAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'rdi']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__']


@admin.register(VitaminInProduct)
class VitaminInProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'vitamin', 'amount', 'unit']
    list_select_related = ['product', 'vitamin']
