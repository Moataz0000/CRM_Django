from django.db import models

class Categorie(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
   
    class Meta:
        ordering = ['-creation_date']
   
    def __str__(self):
        return self.name






class Record(models.Model):
    
  
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name    = models.CharField(max_length=250)
    last_name     = models.CharField(max_length=250)
    category      = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
    tall          = models.IntegerField()
    weight        = models.IntegerField()
    phone         = models.IntegerField()
    address       = models.CharField(max_length=300)
    price         = models.CharField(max_length=200)



    def __str__(self):
        return self.first_name + " " + self.last_name 
    
    class Meta:
        ordering = ['-creation_date']