from django.contrib import admin
from .models import Record, Categorie
# Register your models here.



@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
    

@admin.register(Categorie)
class CategoriesAdmin(admin.ModelAdmin):
    pass    