from django.contrib import admin
from .models import Blog,Publisher,BlogComment
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin	

# Register your models here.
admin.site.register(Blog)
admin.site.register(Publisher)
admin.site.register(BlogComment)


# class CartInline(StackedInlineJalaliMixin, admin.StackedInline):
# 	model = BlogComment

# @admin.register(BlogComment)
# class BlogCommentModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
#     @admin.display(description='تاریخ ایجاد', ordering='created')
#     def get_created_jalali(self, obj):
#         return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')