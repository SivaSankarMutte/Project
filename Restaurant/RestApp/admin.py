from django.contrib import admin
from RestApp.models import Restaurant
from RestApp.models import Item,User
# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(User)