from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    #tutaj przekminiam

    # main page
    url(r'^$', views.ItemView.as_view(), name='item-view'),

    # /items/
    url(r'items/$', views.ItemView.as_view(), name='item-view'),

    # /items/3
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name="itemdetail"),

    # /items/add
    url(r'items/add/$', views.ItemCreate.as_view(), name='item-add'),




]

