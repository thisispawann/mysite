from django.contrib import admin
from . import models

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# Added meta data to admin area
@admin.register(models.Post)
class AuthorAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'slug', 'author')
    prepopulated_fields = {
        "slug": ("title",),
    }
    summernote_fields = ('content',)

#including comment to admin section
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status')
    list_filter = ('status','publish')
    search_fields = ('name', 'email', 'your_comment')


#register category model
admin.site.register(models.Category)
