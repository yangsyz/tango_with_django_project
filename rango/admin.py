from django.contrib import admin
from rango.models import UserProfile
from rango.models import Category, Page

# Register your models here.

class CategotyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category']}),
        (None, {'fields': ['title']}),
        (None, {'fields': ['url']}),
        (None, {'fields': ['views']}),
    ]
    list_display = ('title', 'category', 'url')

admin.site.register(Category, CategotyAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)