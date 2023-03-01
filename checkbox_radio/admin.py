from django.contrib import admin
from .models import Check_box, Radio, Post


@admin.register(Check_box)
class Check_boxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Radio)
class RadioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name_post', 'category', 'Tags')

    def Tags(self,obj):
        return [tag.name for tag in obj.tags.all()]
    