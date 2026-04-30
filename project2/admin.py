from django.contrib import admin
from .models import Category, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publication_date', 'is_featured')
    list_filter = ('category', 'publication_date', 'is_featured')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publication_date'
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'body', 'category')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Publishing', {
            'fields': ('is_featured', 'publication_date', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('publication_date', 'updated_at')

