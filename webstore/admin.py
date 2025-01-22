from django.contrib import admin
from .models import Category, Brand, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class BrandAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "brand", "price",  "quantity", "uploaded_at"]
    list_filter = ["category", "brand", "price", "uploaded_at"]
    search_fields = ["name", "brand", "category"]
    readonly_fields = ["id", "uploaded_at"]
    
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
