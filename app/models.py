from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.city

class Station(models.Model):
    name = models.CharField(max_length=100)
    empty_slots = models.IntegerField()
    free_bikes = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField()

    # Relación con Location
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='stations')

    # Relación con Company (Many-to-Many)
    companies = models.ManyToManyField(Company, related_name='stations')

    def __str__(self):
        return self.name
    
class Sancionatorios(models.Model):
    numero = models.IntegerField()
    expediente = models.CharField(max_length=255)
    unidad_fiscalizable = models.CharField(max_length=255)
    nombre_razon_social = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.numero} - {self.expediente}"