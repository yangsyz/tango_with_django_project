from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

#class CategoryInline(admin.StackedInline):
#    model = Category
#    extra = 3

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category']}),
        (None, {'fields': ['title']}),
        (None, {'fields': ['url']}),
        (None, {'fields': ['views']}),
    ]
    #inlines = [CategoryInline]
    list_display = ('title', 'category', 'url')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)