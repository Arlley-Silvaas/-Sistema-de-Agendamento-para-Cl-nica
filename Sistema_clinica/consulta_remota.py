
from atendimento import Atendimento


class ConsultaRemota(Atendimento):
    def __init__(self, paciente, medico, data_hora, link):
        super().__init__(paciente, medico, data_hora)
        self.link = link

    def detalhes(self):
        return f"Remota - {self.link}"
