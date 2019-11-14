from django.contrib import admin

# Register your models here.
from .models import Shoe,ShoeColor,ShoeType,Manufacturer
admin.site.register(Shoe)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Manufacturer)