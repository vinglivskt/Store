from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')
    search_fields = ('name',)
    ordering = ('name',)


class BacketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', )
    extra = 0
