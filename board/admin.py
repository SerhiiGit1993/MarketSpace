from django.contrib import admin
from .models import *


# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'board_img', 'price',
                    'cat', 'create_date', 'update_date', 'is_published', 'url')
    list_display_links = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description', 'board_img', 'price',
                     'cat', 'create_date', 'update_date', 'is_published', 'url')
    list_editable = ('is_published',)
    list_filter = ('id', 'title', 'description', 'board_img', 'price',
                   'cat', 'create_date', 'update_date', 'is_published', 'url')
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Board, BoardAdmin),
admin.site.register(Category),
admin.site.register(Comments),


