from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from modelos.resultado import Resultado
from bson import ObjectId

class RepositorioResultado(InterfaceRepositorio[Resultado]):
    def getListadoResultadoEnCandidato(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)

    def promedioResultadoEnCandidato(self, id_candidato):
        query1 = {
            "$match": {"candidato.$id": ObjectId(id_candidato)}
        }

        query2 = {
            "$group": {
                "_id": "$candidato",
                "promedio": {
                    "$avg": "$numero_votos"
                }
            }
        }
        pipeline = [query1, query2]
        return self.queryAggregation(pipeline)