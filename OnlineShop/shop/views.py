from django.shortcuts import render,get_object_or_404
from .models import Category, Product
from cart.forms import CartAddForm
# Create your views here.


def home(request, slug=None):
    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.filter(availabel=True)
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    form = CartAddForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'shop/product_detail.html', context)

