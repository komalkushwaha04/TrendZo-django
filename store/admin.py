from django.contrib import admin
from .models import Product,Variation
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'is_available', 'category',  'modified_date')
    prepopulated_fields = {'slug': ('product_name',)}
    

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'Variation_category','Variation_value','is_active')
    list_editable=('is_active',)
    list_filter=('product','Variation_category','Variation_value','is_active')


admin.site.register(Product, ProductAdmin) 
admin.site.register(Variation,VariationAdmin)