
from datetime import datetime, timedelta
from clinica import Clinica
from interface import Interface


sistema = Clinica()

# Pacientes para teste
sistema.cadastrar_paciente("Ana Souza", "11111111111", "99999-1111")
sistema.cadastrar_paciente("Pedro Lima", "22222222222", "99999-2222")
sistema.cadastrar_paciente("Maria Costa", "33333333333", "99999-3333")

# Médicos para teste
sistema.cadastrar_medico("Carlos Mendes", "CRM123", "Cardiologia")
sistema.cadastrar_medico("Julia Alves", "CRM456", "Dermatologia")
sistema.cadastrar_medico("Roberto Silva", "CRM789", "Pediatria")

# Consulta de teste para o dia seguinte
proxima_hora = (
    datetime.now().replace(minute=0, second=0, microsecond=0)
    + timedelta(hours=1)
)

sistema.agendar(
    "11111111111",
    "CRM123",
    proxima_hora,
    "Presencial",
    "Sala 02"
)

sistema.agendar(
    "22222222222",
    "CRM456",
    proxima_hora + timedelta(hours=1),
    "Remota",
    "https://meet.google.com/exemplo"
)

Interface(sistema).iniciar()
