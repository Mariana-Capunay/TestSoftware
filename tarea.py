import csv
import requests
import time
class Ciudad:
    def __init__(self, nombre_ciudad, nombre_pais):
        self.nombre_ciudad = nombre_ciudad
        self.nombre_pais = nombre_pais

class Coordenada:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

class CoordenadasDesdeCSV:
    def __init__(self, csv_path):
        self.csv_path = csv_path

    def obtener_coordenadas(self, ciudad):
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                if row["city"].lower() == ciudad.nombre_ciudad.lower() and row["country"].lower() == ciudad.nombre_pais.lower():
                    return Coordenada(float(row["lat"]), float(row["lng"]))
        return None


class CoordenadasDesdeAPI:
    def obtener_coordenadas(self, ciudad):
        url = f"https://nominatim.openstreetmap.org/search?q={ciudad.nombre_ciudad},{ciudad.nombre_pais}&format=json"
        response = requests.get(url)
        #print(response.text)
        data = response.json()
        if data:
            return Coordenada(float(data[0]["lat"]), float(data[0]["lon"]))
        return None
    
class CoordenadasMock:
    def obtener_coordenadas(self, ciudad):
        Lima = Coordenada (-12.1, -77.0)
        Cusco = Coordenada (-13.5, -72)
        if ciudad.nombre_ciudad=="Lima":
            return Lima
        
        if ciudad.nombre_ciudad=="Cusco":
            return Cusco
    
import math

def calcular_distancia(coord1, coord2):
    R = 6371  # Radio de la Tierra en km
    lat1, lon1 = math.radians(coord1.latitud), math.radians(coord1.longitud)
    lat2, lon2 = math.radians(coord2.latitud), math.radians(coord2.longitud)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distancia = R * c
    return distancia

class ObtenerCoordenadas:
    def __init__(self, strategy):
        self.strategy = strategy

    def obtener_coordenadas(self, ciudad):
        return self.strategy.obtener_coordenadas(ciudad)


ciudad1 = Ciudad("Lima", "Peru")
ciudad2 = Ciudad("Cusco", "Peru")


if __name__ == "__main__":

    coord1 = coord2 = 0

    opc = int(input("Opcion: "))
    
    def opc1():
        coordenadas_csv = ObtenerCoordenadas(CoordenadasDesdeCSV('worldcities.csv'))
        coord1 = coordenadas_csv.obtener_coordenadas(ciudad1)
        coord2 = coordenadas_csv.obtener_coordenadas(ciudad2)
    
        print("Coordenadas desde CSV:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        return coord1, coord2

    def opc2():
        coordenadas_api = ObtenerCoordenadas(CoordenadasDesdeAPI())
        coord1 = coordenadas_api.obtener_coordenadas(ciudad1)
        time.sleep(3)
        coord2 = coordenadas_api.obtener_coordenadas(ciudad2)

        print("Coordenadas desde API:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        return coord1, coord2

    def opc3():
        coordenadas_mock = ObtenerCoordenadas(CoordenadasMock())
        coord1 = coordenadas_mock.obtener_coordenadas(ciudad1)
        coord2 = coordenadas_mock.obtener_coordenadas(ciudad2)

        print("Coordenadas mock:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        return coord1, coord2

    if opc==1: 
        coord1, coord2 = opc1()
    elif opc==2: 
        coord1, coord2 = opc2()
    else: 
        coord1, coord2 = opc3()


    if coord1 and coord2:
        distancia = calcular_distancia(coord1, coord2)
        print(f"La distancia entre {ciudad1.nombre_ciudad} y {ciudad2.nombre_ciudad} es {distancia:.2f} km.")
    else:
        print("No se pudieron obtener las coordenadas de una o ambas ciudades.")
