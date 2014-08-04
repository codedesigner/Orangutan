from django.conf.urls import patterns, url
from products import views

urlpatterns = patterns('',
    url(r'^(?P<product_id>\d+)$', views.index, name='index'),
)