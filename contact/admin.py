from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'category', 'show',)
    ordering = ('first_name', 'id',)
    search_fields = ("id", "first_name", "last_name", 'category')
    list_filter = ('category', 'created_date')
    list_per_page = 8
    list_max_show_all = 100
    list_editable = ('show',)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    ordering = ('name', 'id',)
