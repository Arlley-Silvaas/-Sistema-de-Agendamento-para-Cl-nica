
from datetime import datetime, time, timedelta
from paciente import Paciente
from medico import Medico
from consulta_presencial import ConsultaPresencial
from consulta_remota import ConsultaRemota


class Clinica:
    def __init__(self):
        self.__pacientes = []
        self.__medicos = []
        self.__atendimentos = []

    def cadastrar_paciente(self, nome, cpf, telefone):
        # Verifica se os campos foram preenchidos
        if not nome.strip() or not cpf.strip() or not telefone.strip():
            raise ValueError("Preencha todos os campos.")

        if not cpf.isdigit() or len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 números.")

        if any(p.cpf == cpf for p in self.__pacientes):
            raise ValueError("CPF já cadastrado.")

        self.__pacientes.append(Paciente(nome, cpf, telefone))

    def cadastrar_medico(self, nome, crm, especialidade):
        # Verifica se os campos foram preenchidos
        if not nome.strip() or not crm.strip() or not especialidade.strip():
            raise ValueError("Preencha todos os campos.")

        if any(m.crm == crm for m in self.__medicos):
            raise ValueError("CRM já cadastrado.")

        self.__medicos.append(Medico(nome, crm, especialidade))

    def buscar_paciente(self, cpf):
        return next((p for p in self.__pacientes if p.cpf == cpf), None)

    def buscar_medico(self, crm):
        return next((m for m in self.__medicos if m.crm == crm), None)

    def listar_pacientes(self):
        return self.__pacientes.copy()

    def listar_medicos(self):
        return self.__medicos.copy()

    def listar_atendimentos(self):
        return self.__atendimentos.copy()

    def horario_disponivel(self, medico, data_hora, ignorar=None):
        return not any(
            a is not ignorar and a.medico == medico
            and a.data_hora == data_hora and a.status == "Agendado"
            for a in self.__atendimentos
        )

    def agendar(self, cpf, crm, data_hora, tipo, detalhe):
        paciente = self.buscar_paciente(cpf)
        medico = self.buscar_medico(crm)

        if tipo not in ("Presencial", "Remota"):
         raise ValueError("Selecione um tipo de consulta válido.")

        if not detalhe.strip():
            raise ValueError("Informe a sala ou o link da consulta.")
        
        if not paciente or not medico:
            raise ValueError("Paciente ou médico não encontrado.")

        if data_hora <= datetime.now():
            raise ValueError("Escolha uma data futura.")

        if not self.horario_disponivel(medico, data_hora):
            raise ValueError("Horário já ocupado para esse médico.")

        if tipo == "Presencial":
            atendimento = ConsultaPresencial(
                paciente, medico, data_hora, detalhe
            )
        else:
            atendimento = ConsultaRemota(
                paciente, medico, data_hora, detalhe
            )

        self.__atendimentos.append(atendimento)

    def consultar_horarios(self, crm, data):
        medico = self.buscar_medico(crm)

        if not medico:
            raise ValueError("Médico não encontrado.")

        horarios = []
        inicio = datetime.combine(data, time(8))
        fim = datetime.combine(data, time(18))

        while inicio < fim:
            if inicio > datetime.now() and self.horario_disponivel(medico, inicio):
                horarios.append(inicio)
            inicio += timedelta(hours=1)

        return horarios

    def cancelar(self, atendimento):
        atendimento.cancelar()

    def remarcar(self, atendimento, nova_data):
        if nova_data <= datetime.now():
            raise ValueError("Escolha uma data futura.")

        if not self.horario_disponivel(
            atendimento.medico, nova_data, atendimento
        ):
            raise ValueError("Horário já ocupado para esse médico.")

        atendimento.remarcar(nova_data)

    def historico(self, cpf):
        paciente = self.buscar_paciente(cpf)

        if not paciente:
            raise ValueError("Paciente não encontrado.")

        return [
            a for a in self.__atendimentos
            if a.paciente == paciente
        ]
