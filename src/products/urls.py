from django.urls import URLPattern
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from products.views import (
    ProductListView, 
    ProductDetailView, 
    DigitalProductListView, 
    ProductIDRedirectView, 
    ProductRedirectView, 
    ProtectedProductDetailView,
    ProtectedProductCreateView,       
    ProtectedProductUpdateView,     # Esta ruta fue creada para poder actualizar productos, se protegió de manera que solo usuarios autenticados puedan actualizar productos
    ProtectedProductDeleteView,      # Esta ruta fue creada para poder eliminar productos, se protegió de manera que solo usuarios autenticados puedan eliminar productos
    ProtectedListView,              # Esta ruta fue creada para poder listar los productos del usuario autenticado, se protegió de manera que solo usuarios autenticados puedan ver sus propios productos
    )    

urlpatterns = [
    path("admin/", admin.site.urls),
    path("about-us", RedirectView.as_view(url="/products/about")),
    path("about", TemplateView.as_view(template_name="products/about.html")),
    path("team", TemplateView.as_view(template_name="products/team.html")),
    path("products/", ProductListView.as_view()), 
    path("digital-products/", DigitalProductListView.as_view()),         
    path("products/<int:pk>/", ProductDetailView.as_view()),
    path("products/<slug:slug>/", ProductDetailView.as_view()),
    path("p/<int:pk>", ProductIDRedirectView.as_view()), 
    path("p/<slug:slug>/", ProductRedirectView.as_view()),

    #path("my-products/<slug:slug>/", ProtectedProductDetailView.as_view()),   
    path("my-products/", ProtectedListView.as_view()),       # Esta ruta fue creada para listar los productos del usuario autenticado, se protegió de manera que solo usuarios autenticados puedan ver sus propios productos
    path("my-products/create/", ProtectedProductCreateView.as_view()),       
    path("my-products/<slug:slug>/", ProtectedProductUpdateView.as_view()),       # Esta ruta fue creada para poder actualizar productos, se protegió de manera que solo usuarios autenticados puedan actualizar productos
    path("my-products/<slug:slug>/delete/", ProtectedProductDeleteView.as_view()),         # Esta ruta fue creada para poder eliminar productos, se protegió de manera que solo usuarios autenticados puedan eliminar productos        
]