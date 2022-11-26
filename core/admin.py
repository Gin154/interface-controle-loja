from django.contrib import admin
from .models import product, client, categ
# Register your models here.
admin.site.register(product)
admin.site.register(categ)
admin.site.register(client)