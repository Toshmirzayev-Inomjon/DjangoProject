from django.contrib import admin
from .models import News, Category, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'subject')

