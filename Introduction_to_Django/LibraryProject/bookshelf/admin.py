from django.contrib import admin

# Register your models here.
from .models import Book
admin.site.register(Book)


class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    # Fields to enable filtering options
    list_filter = ('publication_year',)
    # Fields to enable search functionality
    search_fields = ('title', 'author')
    

admin.site.register(Book, BookAdmin)
