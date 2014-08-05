from django.conf.urls import patterns, url
from products import views

urlpatterns = patterns('',
    url(r'^$', views.products_list, name='products_list'),
)