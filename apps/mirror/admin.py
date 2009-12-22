from mirror.models import Mirror, OS, Product, User, Location
from django.contrib import admin


class LocationAdmin(admin.ModelAdmin):
    list_display = ('product', 'os', 'path', 'lang')
    list_filter = ('product', 'os', 'lang')
admin.site.register(Location, LocationAdmin)

class MirrorAdmin(admin.ModelAdmin):
    list_display = ('active', 'rating', 'name', 'baseurl', 'count')
    list_display_links = ('name',)
    list_filter = ('active',)
    ordering = ('active',)
admin.site.register(Mirror, MirrorAdmin)

class OSAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority')
    ordering = ('priority',)
admin.site.register(OS, OSAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'count', 'active', 'checknow')
    list_filter = ('active', 'checknow')
    ordering = ('name',)
admin.site.register(Product, ProductAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname', 'lastname', 'email', 'converted')
    ordering = ('username',)
admin.site.register(User, UserAdmin)
