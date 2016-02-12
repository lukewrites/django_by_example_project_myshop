from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

    # Notice that the above two patterns call the same view, just one includes the
    # category_slug. Pretty clever, eh? This takes advantage of the logic pointed
    # out in the product_list view.
    

]
