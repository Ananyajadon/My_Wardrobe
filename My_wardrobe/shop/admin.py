from django.contrib import admin
from .models import Product
from .models import FeatProduct


admin.site.register(Product),
admin.site.register(FeatProduct)
