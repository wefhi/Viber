from django.views import generic
from django.views.generic.edit import CreateView
from music.models import Item
from django.core.mail import send_mail
#tutaj sam kombinuje


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
    fields = ['nazwa', 'cena', 'zdjecie']

