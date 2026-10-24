from django.contrib.auth.mixins import LoginRequiredMixin       

from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView, 
    DetailView, 
    RedirectView,
    CreateView,
    UpdateView,     # Esta linea fue creada para poder actualizar productos
    DeleteView,     # Esta linea fue creada para poder eliminar productos  
    )
from django.shortcuts import render, get_object_or_404 , redirect

from .forms import ProductModelForm   
from .models import Product, DigitalProduct
from .mixins import TemplateTitleMixin

# Clase para actualizar productos
class ProtectedProductUpdateView(LoginRequiredMixin, UpdateView):       # Se define la clase ProtectedProductUpdateView que hereda de UpdateView y LoginRequiredMixin
    form_class = ProductModelForm       # Se define el formulario a utilizar
    template_name = "products/product_detail.html"        # Se define la plantilla a utilizar

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)       # Este queryset filtra los productos solo del usuario autenticado
    
    def get_success_url(self):
        return self.object.get_absolute_url()        # Esta linea retorna la url absoluta del producto

# Clase para eliminar productos
class ProtectedProductDeleteView(LoginRequiredMixin, DeleteView):    
    template_name = "forms-delete.html"  
    
    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)       # Este queryset filtra los productos solo del usuario autenticado

    def get_success_url(self):
        return "/products/products/"       # Esta linea retorna la url absoluta del producto

class ProtectedProductCreateView(LoginRequiredMixin, CreateView):
    form_class = ProductModelForm       
    template_name = "forms.html"        

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)   

    def form_invalid(self, form):
        return super().form_invalid(form)       

# Clase para listar los productos del usuario autenticado
class ProtectedListView(LoginRequiredMixin, TemplateTitleMixin, ListView):       # Se define la clase ProtectedListView que hereda de ListView, TemplateTitleMixin y LoginRequiredMixin
    model = Product       # Se define el modelo a utilizar
    template_name = "products/product_list.html"        # Se define la plantilla a utilizar
    title = "Mis Productos"       # Se define el titulo que se mostrara en la plantilla

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)       # Este queryset filtra los productos solo del usuario que hace el request

class ProductIDRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        pk = url_params.get("pk")
        obj = get_object_or_404(Product, pk=pk)
        slug = obj.slug
        return f"/products/products/{slug}/"

class ProductRedirectView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url_params = self.kwargs
        slug = url_params.get("slug")
        return f"/products/products/{slug}/"
        

class ProductListView(TemplateTitleMixin, ListView):    
    model = Product
    title = "Productos Fisicos"                 

class DigitalProductListView(TemplateTitleMixin, ListView):   
    model = DigitalProduct
    template_name = "products/product_list.html"
    title = "Productos Digitales"  

class ProductDetailView(DetailView):  
    model = Product  

class ProtectedProductDetailView(LoginRequiredMixin, DetailView):  
    model = Product                      