from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import ProductModelForm
from .models import ProductModel

from django.db.models import Q  


# Create your views here.

# Vista para eliminar de un producto
def product_model_delete_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    if request.method == "POST":
        instance.delete()
        messages.success(request, "Producto eliminado con exito")
        return HttpResponseRedirect("/ecommerce")

    context = {
        "product": instance
    }
    template = "ecommerce/delete-view.html"
    return render(request, template, context)


# Vista de actualizacion de un producto
def product_model_update_view(request, product_id = None):
    instance = get_object_or_404(ProductModel, id=product_id)
    form = ProductModelForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto actualizado con exito")
        return HttpResponseRedirect("/ecommerce/{product_id}".format(product_id=instance.id))

    context = {
        "form": form
    }
    template = "ecommerce/update-view.html"
    return render(request, template, context)        


# Vista de creacion de un producto
def product_model_create_view(request):
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Producto creado con exito")
        return HttpResponseRedirect("/ecommerce/{product_id}".format(product_id=instance.id))

    context = {
        "form": form
    }

    template = "ecommerce/create-view.html"
    return render(request, template, context)        
    

# Vista de detalle de un producto
def product_model_detail_view(request, product_id):
    instance = get_object_or_404(ProductModel, id=product_id)
    context = {
        "product": instance
    }
    template = "ecommerce/detail-view.html"
    return render(request, template, context)


# Vista de listado de productos
def product_model_list_view(request):
    query = request.GET.get("q", None) 
    queryset = ProductModel.objects.all()
    if query is not None:
        queryset = queryset.filter(
            Q(title__icontains=query) | 
            Q(price__icontains=query) | 
            Q(description__icontains=query) | 
            Q(seller__icontains=query) | 
            Q(color__icontains=query) | 
            Q(product_dimensions__icontains=query) 
        )
    template = "ecommerce/list-view.html"
    context = {
        "products": queryset        
    }
 
    if request.user.is_authenticated:    
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-view-public.html"

    return render(request, template, context)  

# Vista protegida solo para usuarios autenticados
@login_required  
def login_required_view(request):
    queryset = ProductModel.objects.all()
    template = "ecommerce/list-view.html"
    context = {
        "products": queryset        
    }

    if request.user.is_authenticated:     
        template = "ecommerce/list-view.html"
    else:
        template = "ecommerce/list-view-public.html"

    return render(request, template, context)    