from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='shopindex'),
    path('about/', views.about, name='AboutUs'),
    path('create/', views.create, name='create'),
    path('contact/', views.contact, name='ContactUs'),
    path('search/', views.search, name='Search'),
    path('productview/', views.productview, name='ProductView'),
    path('checkout/', views.checkout, name='CheckOut'),
    path('tracker/', views.tracker, name='Tracker'),
]
urlpatterns += staticfiles_urlpatterns()