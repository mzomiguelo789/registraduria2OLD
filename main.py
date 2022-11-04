from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://ciclo4:ciclo4@cluster0.kzfcwiy.mongodb.net/registraduria?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.test
print(db)

baseDatos = client["registraduria"]
print(baseDatos.list_collection_names())


app = Flask(__name__)
cors = CORS(app)
from controladores.controladorPartido import ControladorPartido
miControladorPartido = ControladorPartido()

from controladores.controladorMesa import ControladorMesa
miControladorMesa = ControladorMesa()

from controladores.controladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

from controladores.controladorResultado import ControladorResultado
miControladorResultado = ControladorResultado()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

#pagina de partido
@app.route("/partidos",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)
@app.route("/partidos",methods=['POST'])
def crearPartidos():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)
@app.route("/partidos/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

#pagina de mesas
@app.route("/mesas",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)
@app.route("/mesas",methods=['POST'])
def crearMesas():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['PUT'])
def modificarMesas(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)
@app.route("/mesas/<string:id>",methods=['DELETE'])
def eliminarMesas(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

#pagina de candidato
@app.route("/candidatos",methods=['GET'])
def getCandidatos():
    json=miControladorCandidato.index()
    return jsonify(json)
@app.route("/candidatos",methods=['POST'])
def crearCandidatos():
    data = request.get_json()
    json=miControladorCandidato.create(data)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['GET'])
def getCandidato(id):
    json=miControladorCandidato.show(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>",methods=['PUT'])
def modificarCandidatos(id):
    data = request.get_json()
    json=miControladorCandidato.update(id,data)
    return jsonify(json)
@app.route("/cadidatos/<string:id>",methods=['DELETE'])
def eliminarCandidatos(id):
    json=miControladorCandidato.delete(id)
    return jsonify(json)
@app.route("/candidatos/<string:id>/partido/<string:id_partido>",methods=['PUT'])
def asignarCandidatosAPartido(id, id_partido):
    json=miControladorCandidato.asignarPartido(id, id_partido)
    return jsonify(json)



#paginas de resultados
@app.route("/resultados",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)
@app.route("/resultados/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['POST'])
def crearResultados(id_mesa, id_candidato):
    data = request.get_json()
    json=miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)
@app.route("/resultados/<string:id>/mesa/<string:id_mesa>/candidato/<string:id_candidato>",methods=['PUT'])
def modificarResultados(id_resultado, id_mesa, id_candidato):
    data = request.get_json()
    json=miControladorResultado.update(data, id_resultado, id_mesa, id_candidato)
    return jsonify(json)
@app.route("/resultados/<string:id_resultado>",methods=['DELETE'])
def eliminarResultados(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)
@app.route("/resultados/candidato/<string:id_candidato>",methods=['GET'])
def resultadoEnCandidato(id_candidato):
    json=miControladorResultado.listarResultadoEnCandidato(id_candidato)
    return jsonify(json)
@app.route("/resultados/promedio/candidato/<string:id_candidato>",methods=['GET'])
def getPromedioCandidato(id_candidato):
    json=miControladorResultado.promedioResultadoEnMateria(id_candidato)
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
