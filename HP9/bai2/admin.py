from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'available')
    list_filter = ('created_at', 'available')
    search_fields = ('title', 'author')
    ordering = ('title',)  # Corrected the typo here
