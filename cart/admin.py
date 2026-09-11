from django.contrib import admin


from .models import Order, Item

class ItemInline(admin.TabularInline):
    model = Item
    raw_id = ['movie']
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'date')
    list_filter = ('date', )
    search_fields = ('user__username', 'id')
    inlines = [ItemInline]

admin.site.register(Order, OrderAdmin)
admin.site.register(Item)