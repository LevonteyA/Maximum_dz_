from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from .models import OnlineShop

#создаём класс для отбражения в панели администрирования
class OnlineShopAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_time', 'auction', 'image_mini']
    list_filter = ['auction', 'created_time']
    actions = ['make_auction_as_false','make_auction_as_true']

    def image_mini(self, obj):
        return format_html('<img src="{}" width="50" height="50"/>', obj.get_image_url())
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)
#отображаем модель в панели администрирования
admin.site.register(OnlineShop, OnlineShopAdmin)
