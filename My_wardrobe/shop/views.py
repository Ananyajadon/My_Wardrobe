import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, FeatProduct


def index(request):
    products = Product.objects.all()
    feat_products = FeatProduct.objects.all()
    n = len(products)
    print(products)
    all_prods = [[feat_products], [feat_products]]
    params = {'products': products, 'all_prods': all_prods}
    return render(request, 'shop/index.html', params)


def create(request):
    p = Product.objects.create(category="Fiction",
                               sub_category="Thriller",
                               product_name="Harry potter 5",
                               product_price=199,
                               product_desc="This is harry potter 5 book",
                               publish_date=datetime.datetime.now(),
                               image="shop/images/harry5.jpg"
                               )
    print(p)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return render(request, 'shop/contact.html')


def search(request):
    return HttpResponse("We are in search end point")


def productview(request):
    return render(request, 'shop/product_view.html')


def checkout(request):
    return render(request, 'shop/check_out.html')


def tracker(request):
    return render(request, 'shop/tracker.html')
