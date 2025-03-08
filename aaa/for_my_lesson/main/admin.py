from django.contrib import admin
from main.models import Article

class BlogsAdmin(admin.ModelAdmin):  # Название класса лучше писать в CamelCase
    list_display = ('id', 'title')  # Добавил 'title'
    list_display_links = ('id', 'title')  # Теперь 'title' есть в list_display
    search_fields = ('id', 'title')  # Теперь можно искать по title
    list_filter = ('title',)
admin.site.register(Article, BlogsAdmin)
