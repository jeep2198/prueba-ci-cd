from flask import Flask, jsonify, request
import json
import uuid

app = Flask(__name__)

# Datos de ejemplo en un diccionario
datos = []

# Endpoint para obtener todos los datos
@app.route('/api/data', methods=['GET'])
def obtener_datos():
    return jsonify(datos)

# Endpoint para agregar datos (POST)
@app.route('/api/data/agregar', methods=['POST'])
def agregar_datos():
    nuevo_dato = request.json
    nuevo_dato['id'] = str(uuid.uuid4())  # Generar un UUID como identificador único
    datos.append(nuevo_dato)

    
    return jsonify({'mensaje': 'Dato agregado correctamente', 'datos': datos})

# Endpoint para obtener un dato específico por su nombre (GET)
#@app.route('/api/data', methods=['GET'])
# def obtener_dato_por_nombre():
#     nombre = request.args.get('nombre')
#     if nombre:
#         dato = next((dato for dato in datos if dato['nombre'] == nombre), None)
#         if dato:
#             return jsonify(dato)
#         else:
#             return jsonify({'mensaje': 'No se encontró el dato con el nombre proporcionado'})
#     else:
#         return jsonify({'mensaje': 'Proporciona un nombre para buscar el dato'})

@app.route('/api/data/find', methods=['GET'])
def obtener_dato_por_nombre():
    nombre = request.args.get('nombre')
    #return(nombre)
    app.logger.warning(nombre)
    dato_encontrado = [dato for dato in datos if dato.get('nombre') == nombre]
    print(dato_encontrado)
    app.logger.debug(dato_encontrado)
    if dato_encontrado:
        return jsonify(dato_encontrado)
    else:
        return jsonify({'mensaje': 'No se encontró el dato con el nombre proporcionado'})



if __name__ == '__main__':

    app.run(debug=True)
