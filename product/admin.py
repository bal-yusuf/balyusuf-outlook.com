from django.contrib import admin

# Register your models here.
from product.models import Category, Product, Images


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']


class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'product', 'image']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image']
    inlines = [ProductImageInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)