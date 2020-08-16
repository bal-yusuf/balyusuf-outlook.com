from django.contrib import admin
# Register your models here.
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from content.models import Menu, Content, CImages, Comment



class ContentImageInline(admin.TabularInline):
    model = CImages
    extra = 3

class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'user', 'status', 'create_at']
    list_filter = ['status', 'type']
    inlines = [ContentImageInline]

    prepopulated_fields = {'slug': ('title',)}

class MenuAdmin(DraggableMPTTAdmin):

    mptt_indent_field = 'title'

    list_display = ('tree_actions', 'indented_title', 'status')
    list_filter = ['status']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'content', 'user', 'status']
    list_filter = ['status']


admin.site.register(Menu,MenuAdmin)
admin.site.register(Content,ContentAdmin)
admin.site.register(Comment,CommentAdmin)
