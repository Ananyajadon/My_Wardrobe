import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, FeatProduct


def index(request):
    products = Product.objects.all()
    feat_products = FeatProduct.objects.all()
    Fiction_category = FeatProduct.objects.filter(IsFiction="True")
    nonFiction_category = FeatProduct.objects.filter(IsFiction="False")

    # logic for new_arrivals start from here
    all_dates = FeatProduct.objects.values_list("publish_date")
    from_date = datetime.date.today() - datetime.timedelta(days=7)
    # newArrivals() function
    new_arrivals = newArrivals(all_dates, from_date)
    # logic for new_arrivals ends here

    all_prods = [[Fiction_category], [nonFiction_category]]
    params = {'products': products, 'all_prods': all_prods, 'new_arrivals1': new_arrivals[:int(len(new_arrivals) / 2)],
              'new_arrivals2': new_arrivals[int(len(new_arrivals) / 2):]}
    return render(request, 'shop/index.html', params)


def create(request):
    p = FeatProduct.objects.create(
        IsFiction=False,
        category="Non-Fiction",
        sub_category="Educational",
        product_name="The Art Of Peace",
        product_price=229,
        product_desc="For over a century, Sun Tzu's writings in The Art of War a have been studied by millions of people from business leaders to military strategists. It occurred to me that Sun Tzu's writings not only provide guidance in warfare strategies, but also for individuals who are battling their own personal demons and desire greater peace.",
        publish_date=datetime.datetime(2023, 3, 2),
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


def newArrivals(all_dates, from_date):
    """
    this 'newArrivals' function is used to filter last 7 days books that've listed
    all_dates: gives all the date with in the database
    from_date: gives the date from which the books should be showing till present date
    """
    new_arrivals = []
    sorted_dates = []
    for date in all_dates:
        if date not in sorted_dates:
            sorted_dates.append(date)

    for dates in sorted_dates:
        for date in dates:
            if date > from_date:
                book = FeatProduct.objects.filter(publish_date=date)
                new_arrivals.append(book)
    return new_arrivals
