from modelos.candidato import Candidato
from modelos.partido import Partido
from Repositorios.repositorioCandidato import RepositorioCandidato
from Repositorios.repositorioPartido import RepositorioPartido

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        elCandidato = Candidato(infoCandidato)
        return self.repositorioCandidato.save(elCandidato)

    def show(self, id):
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoAcual = Candidato(self.repositorioCandidato.findById(id))
        candidatoAcual.cedula = infoCandidato["cedula"]
        candidatoAcual.numero_resolucion = infoCandidato["numero resolucion"]
        candidatoAcual.nombre = infoCandidato["nombre"]
        candidatoAcual.apellidos = infoCandidato["lema"]
        return self.repositorioCandidato.save(candidatoAcual)

    def delete(self, id):
        return self.repositorioCandidato.delete(id)

    """
    Relación candidato y partido
    """
    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido =partidoActual
        return self.repositorioCandidato.save(candidatoActual)
