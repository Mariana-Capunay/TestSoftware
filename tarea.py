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
        Arequipa = Coordenada (-16.4, -71.5)

        if ciudad.nombre_ciudad=="Lima":
            return Lima
        
        elif ciudad.nombre_ciudad=="Cusco":
            return Cusco
        elif ciudad.nombre_ciudad=="Arequipa":
            return Arequipa
    
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

def calcular_minima_distancia_entre_tres(ciudad1, ciudad2, ciudad3, obtener_coordenadas):
    coord1 = obtener_coordenadas.obtener_coordenadas(ciudad1)
    coord2 = obtener_coordenadas.obtener_coordenadas(ciudad2)
    coord3 = obtener_coordenadas.obtener_coordenadas(ciudad3)

    if coord1 and coord2 and coord3:
        distancia1_2 = calcular_distancia(coord1, coord2)
        distancia1_3 = calcular_distancia(coord1, coord3)
        distancia2_3 = calcular_distancia(coord2, coord3)
        
        distancia_minima = min(distancia1_2, distancia1_3, distancia2_3)
        
        return distancia_minima
    else:
        return None

ciudad1 = Ciudad("Lima", "Peru")
ciudad2 = Ciudad("Cusco", "Peru")
ciudad3 = Ciudad("Arequipa", "Peru")


if __name__ == "__main__":

    coord1 = coord2 = 0

    opc = int(input("Opcion: "))
    
    def opc1():
        coordenadas_csv = ObtenerCoordenadas(CoordenadasDesdeCSV('worldcities.csv'))
        coord1 = coordenadas_csv.obtener_coordenadas(ciudad1)
        coord2 = coordenadas_csv.obtener_coordenadas(ciudad2)
        coord3 = coordenadas_csv.obtener_coordenadas(ciudad3)
    
        print("Coordenadas desde CSV:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        print(coord3.latitud, coord3.longitud)
        return coord1, coord2, coord3

    def opc2():
        coordenadas_api = ObtenerCoordenadas(CoordenadasDesdeAPI())
        coord1 = coordenadas_api.obtener_coordenadas(ciudad1)
        time.sleep(3)
        coord2 = coordenadas_api.obtener_coordenadas(ciudad2)
        time.sleep(3)
        coord3 = coordenadas_api.obtener_coordenadas(ciudad3)
        
        print("Coordenadas desde API:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        print(coord3.latitud, coord3.longitud)
        return coord1, coord2, coord3

    def opc3():
        coordenadas_mock = ObtenerCoordenadas(CoordenadasMock())
        coord1 = coordenadas_mock.obtener_coordenadas(ciudad1)
        coord2 = coordenadas_mock.obtener_coordenadas(ciudad2)
        coord3 = coordenadas_mock.obtener_coordenadas(ciudad3)

        print("Coordenadas mock:")
        print(coord1.latitud, coord1.longitud)
        print(coord2.latitud, coord2.longitud)
        print(coord3.latitud, coord3.longitud)
        return coord1, coord2, coord3

    if opc==1: 
        coord1, coord2, coord3 = opc1()
    elif opc==2: 
        coord1, coord2, coord3 = opc2()
    else: 
        coord1, coord2, coord3 = opc3()


    if coord1 and coord2 and coord3:
        distancia_minima = calcular_minima_distancia_entre_tres(coord1, coord2)
        print(f"La distancia mínima entre {ciudad1.nombre_ciudad} y {ciudad2.nombre_ciudad} y {ciudad3.nombre_ciudad} es {distancia_minima} km.")
    else:
        print("No se pudieron obtener las coordenadas de una o más ciudades.")
