from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category, Order
from .forms import OrderForms


def home(request):
    featured_products = Product.objects.filter(
        is_active=True
    ).order_by('?')[:4]
    categories = Category.objects.all()[:4]     
    return render(request, 'core/home.html', {'featured_products':featured_products,'categories':categories})

def shop(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    search_query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category')
    if search_query:
        products = products.filter(Q(name__icontains=search_query)|Q(description__icontains=search_query)|Q(category__name__icontains=search_query))
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, 'core/shop.html', {'products': products,'categories': categories,'search_query': search_query})

def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk,is_active=True)
    return render(request,'core/product_detail.html',{'product': product})

def order(request, pk):
    product = get_object_or_404(Product,pk=pk,is_active=True)
    if request.method == 'POST':
        form = OrderForms(request.POST)
        if form.is_valid():
            order_instance = form.save(commit=False)
            order_instance.product = product
            order_instance.save()
            return redirect('order_success', pk=order_instance.pk)
    else:
        form = OrderForms()
        return render(request, 'core/order.html', {'product':product, 'form':form})
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request,'core/order_success.html',{'order':order})

