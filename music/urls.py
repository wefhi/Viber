from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [

    #tutaj przekminiam

    # /music/items/
    url(r'items/$', views.ItemView.as_view(), name='item-view'),

    # /music/items/3
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetailView.as_view(), name="itemdetail"),

    # /music/items/add
    url(r'items/add/$', views.ItemCreate.as_view(), name='item-add'),
]

