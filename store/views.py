from django.shortcuts import get_object_or_404, render

from .models import Product


def landing_page(request):
    return render(request, 'home.html')


def gallery(request):
    products = Product.products.all()
    return render(request, 'gallery.html', {'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'product.html', {'product': product})