from django.contrib import admin
from .models import FinData, Category, FinDataGroup


admin.site.register(FinData)
admin.site.register(FinDataGroup)
admin.site.register(Category)
