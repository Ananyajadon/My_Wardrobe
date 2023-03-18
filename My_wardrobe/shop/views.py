import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, FeatProduct


def index(request):
    products = Product.objects.all()
    # feat_products = FeatProduct.objects.all()
    Fiction_category = FeatProduct.objects.filter(IsFiction="True")
    nonFiction_category = FeatProduct.objects.filter(IsFiction="False")

    # category = []
    # cat_prod = FeatProduct.objects.values('category')
    # cats = {item['category'] for item in cat_prod}
    # for cat in cats:
    #     cat = FeatProduct.objects.filter(category=cat)
    #     category.append([cat])

    all_prods = [[Fiction_category], [nonFiction_category]]
    params = {'products': products, 'all_prods': all_prods}
    return render(request, 'shop/index.html', params)


def create(request):
    p = FeatProduct.objects.create(
                               IsFiction=False,
                               category="Non-Fiction",
                               sub_category="Educational",
                               product_name="The Art Of Peace",
                               product_price=229,
                               product_desc="For over a century, Sun Tzu's writings in The Art of War a have been studied by millions of people from business leaders to military strategists. It occurred to me that Sun Tzu's writings not only provide guidance in warfare strategies, but also for individuals who are battling their own personal demons and desire greater peace.",
                               publish_date=datetime.datetime.now(),
                               image="shop/images/The Art Of Peace.jpg"
                               )

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
