from django.contrib import admin
from .models import Restaurant, Menu, MenuItem, Vote
from users.models import CustomUser

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'created_by')
    search_fields = ('name', 'address')
    list_filter = ('created_by',)


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'date')
    inlines = [MenuItemInline]
    date_hierarchy = 'date'
    list_filter = ('restaurant',)


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'menu', 'voted_at')
    list_filter = ('menu__restaurant',)