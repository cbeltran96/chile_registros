from django.shortcuts import render
from .models import Company, Location, Station, Sancionatorios

import requests
import json
from bs4 import BeautifulSoup
from unidecode import unidecode

def index(request):
 
    return render(request, 'home.html')



def bikes(request):
    
    if Company.objects.exists() and Location.objects.exists() and Station.objects.exists():
        companies = Company.objects.all()
        locations = Location.objects.all()
        stations = Station.objects.all()
        return render(request, 'bikes.html', {'companies': companies, 'locations': locations, 'stations': stations})
    
    else:

        url = "https://api.citybik.es/v2/networks/bikerio"
        response = requests.get(url)
        api_data = response.json()

        # Obtener datos relevantes
        network_data = api_data.get("network", {})
        companies_data = network_data.get("company", [])
        location_data = network_data.get("location", {})
        stations_data = network_data.get("stations", [])

        # Crear y guardar las compañias
        for company_name in companies_data:
            company, _ = Company.objects.get_or_create(name=company_name)

        # Crear y guardar la ubicacion
        location = Location.objects.create(
            city=location_data.get("city"),
            country=location_data.get("country"),
            latitude=location_data.get("latitude"),
            longitude=location_data.get("longitude")
        )

        # Crear y guardar las estaciones
        for station_data in stations_data:
            station = Station.objects.create(
                name=station_data.get("name"),
                empty_slots=station_data.get("empty_slots"),
                free_bikes=station_data.get("free_bikes"),
                latitude=station_data.get("latitude"),
                longitude=station_data.get("longitude"),
                timestamp=station_data.get("timestamp"),
                location=location
            )

            # Agregar compañias a la estacion
            for company_name in station_data.get("company", []):
                company = Company.objects.get(name=company_name)
                station.companies.add(company)

        companies = Company.objects.all()
        locations = Location.objects.all()
        stations = Station.objects.all()
        return render(request, 'bikes.html', {'companies': companies, 'locations': locations, 'stations': stations})


def sancionatorio(request):
    if Sancionatorios.objects.exists():
        sanciones = Sancionatorios.objects.all()
        return render(request, 'sanciones.html', {'sanciones': sanciones})
    
    else:
        url = "https://snifa.sma.gob.cl/Sancionatorio/Resultado"
        response = requests.get(url)
        html_content = response.content

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table") 

        rows = table.find_all("tr")  # Encuentra todas las filas

        data = []
        # Recorre todas las filas, excepto la cabecera
        for row in rows[1:]:
            columns = row.find_all("td")  

            # Extrae los datos de cada columna y aplicamos unidecode para los datos con caracteres especiales
            numero_row = unidecode(columns[0].get_text(strip=True))
            expediente_row = unidecode(columns[1].get_text(strip=True))
            unidad_fiscalizable_row = unidecode(columns[2].find("a").get_text(strip=True))
            nombre_razon_social_row = unidecode(columns[3].find("li").get_text(strip=True))
            categoria_row = unidecode(columns[4].find("li").get_text(strip=True))
            region_row = unidecode(columns[5].find("li").get_text(strip=True))
            estado_row = unidecode(columns[6].get_text(strip=True))

            #Guardamos la data en la bd
            Sancionatorios.objects.create(
                    numero = numero_row,
                    expediente = expediente_row,
                    unidad_fiscalizable = unidad_fiscalizable_row,
                    nombre_razon_social = nombre_razon_social_row,
                    categoria = categoria_row,
                    region = region_row,
                    estado = estado_row
                )

            #Armamos el json
            fila = {
                "numero": numero_row,
                "expediente": expediente_row,
                "unidad_fiscalizable": unidad_fiscalizable_row,
                "nombre_razon_social": nombre_razon_social_row,
                "categoria": categoria_row,
                "region": region_row,
                "estado": estado_row,
            }

            data.append(fila)

        json_data = json.dumps(data)

        #guardamos el archivo json
        with open("datos.json", "w") as file:
            file.write(json_data)


        sanciones = Sancionatorios.objects.all()

        return render(request, 'sanciones.html', {'sanciones': sanciones})