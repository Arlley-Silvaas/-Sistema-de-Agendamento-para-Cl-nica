
class Medico:
    def __init__(self, nome, crm, especialidade):
        self.__nome = nome
        self.__crm = crm
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome

    @property
    def crm(self):
        return self.__crm

    @property
    def especialidade(self):
        return self.__especialidade
