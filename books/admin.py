from django.contrib import admin
from .models import Book
# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'author', 'price']
    list_filter = ['title', 'author', 'price']