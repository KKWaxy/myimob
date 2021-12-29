from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

class Illustration(models.Model):
    pass

class Category(models.Model):
    pass
class House(models.Model):
    address = models.CharField(_("Adresse"), max_length=500, null=True, blank=True)
    LotSize = models.CharField(_("Taille du lot"), max_length=600, null=True, blank=True)
    latitude = models.CharField(_("Latitude"), max_length=10, null=True, blank=True)
    longitude = models.CharField(_("Longitude"), max_length=10, null=True, blank=True)
    numeroLot = models.CharField(_("Numéro du Lot"), max_length=20, null=True, blank=True)
    label = models.CharField(_("Libelle"), max_length=200)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    create_date =  models.DateTimeField(_("Created Date"), auto_now_add=True)
    update_date = models.DateTimeField(_("Updated Date"), auto_now=True)
    
    class Meta:
        ordering = ["create_date"]
        
    def __str__(self):
        return self.label
    
    