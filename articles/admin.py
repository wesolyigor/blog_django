from django.contrib import admin

# Register your models here.
from articles.models import Article, Test


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status', 'category')
    list_filter = ('status', 'created', 'publish', 'author', 'category')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


admin.site.register(Test)
