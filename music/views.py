from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.urls import reverse_lazy
from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']



#tutaj sam kombinuje

from .models import Item
from django.views.generic.detail import DetailView

class ItemView(generic.ListView):
    template_name = "music/itemIndex.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailView(DetailView):
    model = Item
    template_name = 'music/itemDetail.html'


class ItemCreate(CreateView):
    model = Item
    fields = ['name', 'price']

