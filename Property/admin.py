from django.contrib import admin
from django.contrib.admin.decorators import register
from . models import Contact, FavouriteProperty, Property, Property_Detail, Role, User,Apartment_Type
# # Register your models here.

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Property)
admin.site.register(Property_Detail)
admin.site.register(Contact)
admin.site.register(FavouriteProperty)
admin.site.register(Apartment_Type)