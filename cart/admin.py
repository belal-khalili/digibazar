from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from .models import Cart,CartItem
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	
# Register your models here.
admin.site.register(CartItem)

class CartInline(StackedInlineJalaliMixin, admin.StackedInline):
	model = Cart

@admin.register(Cart)
class CartModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')