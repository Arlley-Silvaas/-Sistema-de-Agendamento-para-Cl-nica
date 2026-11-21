
from atendimento import Atendimento


class ConsultaPresencial(Atendimento):
    def __init__(self, paciente, medico, data_hora, sala):
        super().__init__(paciente, medico, data_hora)
        self.sala = sala

    def detalhes(self):
        return f"Presencial - Sala {self.sala}"
