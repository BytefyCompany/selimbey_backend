from django.contrib import admin
from .models import Category, Product, User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'user_id']  

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'created_at')  # Removed 'subcategory' from list_display
    list_filter = ('category', 'created_at')  # Removed 'subcategory' from list_filter
    search_fields = ('name', 'description')
    list_per_page = 20

admin.site.register(Category)  # Register Category model
