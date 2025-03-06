from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'price', 'language')
    list_filter = ('publication_date', 'language')
    search_fields = ('title', 'author', 'description')
    ordering = ('-publication_date',)
