from django.shortcuts import render
from .fakedb.products import FAKE_DB_PRODUCTS



def product_list_view(request):
    context = dict(
        products = FAKE_DB_PRODUCTS,
    )
    return render(request, 'products/products.html', context)

def product_detail_view(request,id):
    filtered = list(filter(lambda element: element["id"] == id, FAKE_DB_PRODUCTS ))
    context = dict(
        products = FAKE_DB_PRODUCTS,
        product = filtered[0]
    )
    return render(request, 'products/product_detail.html', context)
