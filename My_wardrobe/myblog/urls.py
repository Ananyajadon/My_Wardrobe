from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='myblogindex')

]
urlpatterns += staticfiles_urlpatterns()