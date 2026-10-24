from django.contrib import admin

# Importar el modelo, el punto hace referencia que el modelo esta dentro del mismo proyecto
from .models import Product, DigitalProduct

# Register your models here.
admin.site.register(Product) # con esto podemos ver el modelo en el panel de admin
admin.site.register(DigitalProduct) # con esto podemos ver el modelo en el panel de admin