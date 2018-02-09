from django.db import models
from django.urls import reverse



#tutaj przekminiam

class Item(models.Model):
    nazwa = models.CharField(max_length=100)
    cena = models.CharField(max_length=30)
    zdjecie = models.FileField()

    def get_absolute_url(self):
        return reverse('music:itemdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name + " - " + self.price