from django.contrib import admin

# Register your models here.
from .models import Category, Blog


admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'category', 'author', 'status']
    search_fields = ['id', 'title']

