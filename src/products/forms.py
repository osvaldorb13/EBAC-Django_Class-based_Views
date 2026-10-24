from django import forms   # Se importa Form para poder crear formularios
from .models import Product      # Se importa el modelo Product para poder crear formularios

class ProductModelForm(forms.ModelForm):   # Se define la clase ProductModelForm que hereda de Form
    class Meta:                 # Se define la clase Meta que hereda de Form para definir el modelo a utilizar y los campos a utilizar
        model = Product         # Se define el modelo a utilizar en este caso es Product
        fields = [              # Se define los campos a utilizar que deben existir en el formulario y en el modelo
            "title",
            "slug",
        ]