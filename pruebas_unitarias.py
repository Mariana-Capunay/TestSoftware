from tarea import Ciudad, Coordenada, CoordenadasDesdeCSV, CoordenadasDesdeAPI, CoordenadasMock, ObtenerCoordenadas, calcular_distancia
import unittest

class TestCoordenadas(unittest.TestCase):

    def setUp(self):
        self.ciudad1 = Ciudad("Lima", "Peru")
        self.ciudad2 = Ciudad("Cusco", "Perú")
        self.ciudad_inexistente = Ciudad("Inexistente", "Peru")
        self.coordenadas_mock = ObtenerCoordenadas(CoordenadasMock())

    def test_caso_exito(self):
        """
         - Caso de exito:
         Definir dos ciudades diferentes y retornar su distancia : Distancia ((lat1, lon1), (lat2,lon2))
         - Test Steps:
          1. Definir el nombre de 2 ciudades y sus respectivos países
          2. Obtener su latitud y longitud (de cada ciudad)
          3. Llamar a la función que calcula la distancia entre 2 ciudades
          4. Ejecutar el programa
         - Test Data:   
           - Ciudad 1: Lima, Perú
           - Ciudad 2: Cusco, Perú
         - Expected Result: distancia entre las 2 ciudades (564.0422180146448)
        """

        coord_ciudad_1 = self.coordenadas_mock.obtener_coordenadas(self.ciudad1)
        coord_ciudad_2 = self.coordenadas_mock.obtener_coordenadas(self.ciudad2)
        
        self.assertIsNotNone(coord_ciudad_1)
        self.assertIsNotNone(coord_ciudad_2)
        
        distancia = calcular_distancia(coord_ciudad_1, coord_ciudad_2)
        self.assertIsNotNone(distancia)
        
        # se espera que la distancia sea: 564.0422180146448
        self.assertEqual(distancia, 564.0422180146448)

    def test_ciudad_inexistente(self):
        """
         - Caso de exito:
         Definir una ciudad existente y otra no y tratar de retornar su distancia : Distancia ((lat1, lon1), None)
         - Test Steps:
          1. Definir el nombre de 1 ciudad y otra no existente
          2. Obtener su latitud y longitud (en ambos casos). En la ciudad inexistente debe retornar None
          3. Llamar a la función que calcula la distancia entre 2 ciudades
          4. Ejecutar el programa
         - Test Data:   
           - Ciudad 1: Lima, Perú
           - Ciudad 2: Inexistente, Perú
         - Expected Result: None (esto se espera que retorna la función, al no poder evaluar)
        """

        coord_ciudad_1 = self.coordenadas_mock.obtener_coordenadas(self.ciudad1)
        coord_ciudad_inexistente = self.coordenadas_mock.obtener_coordenadas(self.ciudad_inexistente)
        
        self.assertIsNotNone(coord_ciudad_1)
        self.assertIsNone(coord_ciudad_inexistente)
        
        distancia = calcular_distancia(coord_ciudad_1, coord_ciudad_inexistente)

        # se espera que la distancia sea None
        self.assertIsNone(distancia)

    def test_misma_ciudad_dos_veces(self):
        """
         - Caso de exito:
         Definir dos veces la misma ciudad : Distancia ((lat1, lon1), (lat2,lon2)), donde lat1=lat2 y lon1=lon2
         - Test Steps:
          1. Definir el nombre de 1 ciudad 
          2. Obtener su latitud y longitud de la ciudad y asignar los mismos valores tanto a la primera como segunda ciudad
          3. Llamar a la función que calcula la distancia entre 2 ciudades
          4. Ejecutar el programa
         - Test Data:   
           - Ciudad 1: Lima, Perú
           - Ciudad 2: Lima, Perú
         - Expected Result: 0 (la distancia desde un punto a sí mismo es 0)
        """
        coord_ciudad_2 = coord_ciudad_1 = self.coordenadas_mock.obtener_coordenadas(self.ciudad1)
        
        self.assertIsNotNone(coord_ciudad_1)
        self.assertIsNotNone(coord_ciudad_2)
        
        distancia = calcular_distancia(coord_ciudad_1, coord_ciudad_2)

        # se espera que la distancia no sea None, que sea 0
        self.assertIsNotNone(distancia)
        self.assertEqual(distancia, 0)

if __name__ == '__main__':
    unittest.main()
