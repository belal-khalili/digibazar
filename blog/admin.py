from django.contrib import admin
from .models import Blog,Publisher,BlogComment
# Register your models here.
admin.site.register(Blog)
admin.site.register(Publisher)
admin.site.register(BlogComment)