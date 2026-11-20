
from abc import ABC, abstractmethod


class Atendimento(ABC):
    def __init__(self, paciente, medico, data_hora):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.status = "Agendado"

    def cancelar(self):
        if self.status != "Agendado":
            raise ValueError("Atendimento não está ativo.")
        self.status = "Cancelado"

    def remarcar(self, data_hora):
        if self.status != "Agendado":
            raise ValueError("Atendimento não está ativo.")
        self.data_hora = data_hora

    @abstractmethod
    def detalhes(self):
        pass
