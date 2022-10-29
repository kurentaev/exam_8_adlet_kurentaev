from django.contrib import admin
from webapp.models import Products, Reviews


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'description', 'image', 'is_deleted']
    list_filter = ['id', 'name', 'category', 'is_deleted']
    search_fields = ['name', 'category', 'is_deleted']
    fields = ['name', 'category', 'description', 'is_deleted']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Products)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'review_text', 'rate', 'is_deleted']
    list_filter = ['id', 'author']
    search_fields = ['author']
    fields = ['author', 'product', 'review_text', 'rate', 'is_deleted']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Reviews, ReviewsAdmin)
