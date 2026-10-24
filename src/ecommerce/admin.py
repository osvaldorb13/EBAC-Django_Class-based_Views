from django.contrib import admin

# Importar el modelo, el punto hace referencia que el modelo esta dentro del mismo proyecto
from .models import ProductModel

# Register your models here.
admin.site.register(ProductModel) # con esto podemos ver el modelo en el panel de admin