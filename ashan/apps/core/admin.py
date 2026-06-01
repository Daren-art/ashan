from django.contrib import admin
from django.contrib import admin
from .models import Category , Order , Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','raiting','is_active','created_at']
    list_filter = ['is_active','category','raiting']
    search_fields = ['name','description']
    list_editable = ['price','is_active']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','email','phone','product','status','created_at']
    list_filter = ['status']
    date_hierarchy = 'created_at'
    list_editable = ['status']
    fieldsets = (('Customer Info', {'fields': ('full_name', 'email', 'phone')}),('Order Details', {'fields': ('product', 'address', 'message')}),('Status', {'fields': ('status',)}),)