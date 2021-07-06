from django.contrib import admin

# Register your models here.
from crud_app.models import Product

admin.site.register(Product)