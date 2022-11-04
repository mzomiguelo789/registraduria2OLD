from modelos.resultado import Resultado
from modelos.mesa import Mesa
from modelos.candidato import Candidato
from Repositorios.repositorioResultado import RepositorioResultado
from Repositorios.repositorioMesa import RepositorioMesa
from Repositorios.repositorioCandidato import RepositorioCandidato

class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioResultado.findAll()

    def create(self, infoResultado, id_mesa, id_candidato):
        elResultado = Resultado(infoResultado)
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)

    def show(self, id):
        elResultado = Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__

    def update(self, id, infoResultado, id_mesa, id_candidato):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        resultadoActual.numero_mesa = infoResultado["numero de mesa"]
        resultadoActual.cedula_candidato = infoResultado["cedula de candidato"]
        resultadoActual.numero_votos = infoResultado["numero de votos"]
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        resultadoActual.mesa = laMesa
        resultadoActual.candidato = elCandidato
        return self.repositorioResultado.save(resultadoActual)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def listarResultadoEnCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoResultadoEnCandidato(id_candidato)
    def promedioResultadoEnMateria(self, id_candidato):
        return self.repositorioResultado.promedioResultadoEnCandidato(id_candidato)