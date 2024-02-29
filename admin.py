from django.contrib import admin
from .models import Product, Lesson, Group

class GroupAdmin(admin.ModelAdmin):
    filter_horizontal = ['users']

admin.site.register(Product)
admin.site.register(Lesson)
admin.site.register(Group, GroupAdmin)
