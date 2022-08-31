from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    catalog_query_all = Phone.objects.all()
    sort = request.GET.get('sort')

    if sort == 'name':
        catalog_query = catalog_query_all.order_by(sort)
    elif sort == 'min_price':
         catalog_query = sorted(catalog_query_all, key=lambda x: x.price, reverse=False)
    elif sort == 'max_price':
         catalog_query = sorted(catalog_query_all, key=lambda x: x.price, reverse=True)
    else:
        catalog_query = Phone.objects.all()

    context = {
        "phones":catalog_query
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    #catalog_query = Phone.objects.filter(slug=slug)

    product_query = get_object_or_404(Phone, slug=slug)
    context = {
        "phone": product_query
    }
    return render(request, template, context)
