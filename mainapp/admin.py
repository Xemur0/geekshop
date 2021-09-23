from django.contrib import admin
from mainapp.models import Product, ProductCategory
from django.contrib.admin import AdminSite
from users.models import Admin

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Product)


class MyAdminSite(AdminSite):
    site_header = 'Your Admin site'

admin_site = MyAdminSite(name='admin')
admin_site.register(Admin)