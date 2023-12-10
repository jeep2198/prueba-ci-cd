import unittest
import json
from main import app
import logging
logging.basicConfig(filename='record.log', level=logging.DEBUG)


class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        # Datos de ejemplo para las pruebas
        self.datos_ejemplo = [
            {'nombre': 'Dato 1'},
            {'nombre': 'Dato 2'}
        ]
    
    def test_obtener_datos(self):
        response = self.app.get('/api/data')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(json.loads(response.data))

    def test_agregar_datos(self):
        nuevo_dato = {'nombre': 'Dato 1'}
        response = self.app.post('/api/data/agregar', json=nuevo_dato)
        self.assertEqual(response.status_code, 200)
        result=json.loads(response.data)['datos']
        
        #print(type(result[0]['nombre']))
        #print(result[0]['nombre'])
        #print(nuevo_dato['nombre'])
        self.assertIn(nuevo_dato['nombre'], result[0]['nombre'])

    def test_obtener_dato_por_nombre_existente(self):
        nombre = 'Dato 1'  # Nombre existente en los datos de ejemplo
        response = self.app.get(f'/api/data/find?nombre={nombre}')
        self.assertEqual(response.status_code, 200)
        result=json.loads(response.data)
        #print(result[0]['nombre'])
        #print(nombre)
        self.assertEqual(result[0]['nombre'], nombre)

    def test_obtener_dato_por_nombre_no_existente(self):
        nombre = 'Dato Inexistente'  # Nombre que no existe en los datos de ejemplo
        response = self.app.get(f'/api/data/find?nombre={nombre}')
        self.assertEqual(response.status_code, 200)
        #print(response.data)
        self.assertEqual(json.loads(response.data), {'mensaje': 'No se encontró el dato con el nombre proporcionado'})

if __name__ == '__main__':
    unittest.main()
