from django.db import models
from django.core.exceptions import ValidationError
import pycountry

class Categorie(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
   
    class Meta:
        ordering = ['-creation_date']
   
    def __str__(self):
        return self.name






class Record(models.Model):
    
    @staticmethod
    def get_country_choices():
        countries = list(pycountry.countries)
        country_choices = [(country.alpha_2, country.name) for country in countries]
        return country_choices


    creation_date = models.DateTimeField(auto_now_add=True)
    first_name    = models.CharField(max_length=250)
    last_name     = models.CharField(max_length=250)
    category      = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
    email         = models.EmailField()
    phone         = models.CharField(max_length=20)
    address       = models.CharField(max_length=300)
    city          = models.CharField(max_length=200)
    province      = models.CharField(max_length=200)
    country       = models.CharField(max_length=2, choices=get_country_choices(), default='EG')


    def __str__(self):
        return self.first_name + " " + self.last_name 
    
    class Meta:
        ordering = ['-creation_date']