from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse


    
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/index2.html', {'product': product})
    
def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        products = products.filter(name__icontains=search)

    if category:
        products = products.filter(category_id=category)

    return render(request, 'catalog/index.html', {
        'products': products,
        'categories': categories
    })
def home(request):
    return HttpResponse('Hello, World!')