from django.contrib import admin
from .models import Article, Caregory, Suggestion, Profile, Comment
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ['profile', 'comment']
    list_display_links = ['profile']
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo']
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['suggestion','user']
    list_display_links = ['suggestion','user']
    list_filter = ['suggestion','user']
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image', 'date', 'text', 'category']
    list_display_links = ['title']
    list_filter = ['date', 'category']
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Caregory, CategoryAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Comment, CommentAdmin)