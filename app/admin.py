from django.contrib import admin
from .models import *

@admin.register(Sancionatorios)
class SancionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'expediente', 'unidad_fiscalizable', 'nombre_razon_social', 'categoria', 'region', 'estado')
    search_fields = ('numero', 'expediente', 'unidad_fiscalizable', 'nombre_razon_social')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('city', 'country', 'latitude', 'longitude')
    search_fields = ('city', 'country')

@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'empty_slots', 'free_bikes', 'latitude', 'longitude', 'timestamp', 'location_id')
    search_fields = ('name', 'empty_slots', 'free_bikes')

