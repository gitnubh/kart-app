from django.contrib import admin
from . models import Categories, Products

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Categories,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','availability','created','updated']
    list_editable = ['price','stock','availability']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Products,ProductAdmin)