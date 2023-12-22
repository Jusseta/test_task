from django.contrib import admin
from payments.models import Item


@admin.register(Item)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price',)
