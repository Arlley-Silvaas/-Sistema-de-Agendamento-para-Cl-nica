# Sistema de Agendamento para Clínica

## 1. Sobre o projeto

Este projeto consiste no desenvolvimento de um sistema de agendamento para clínicas, criado como atividade acadêmica da disciplina de Paradigmas de Programação.

O sistema tem como objetivo facilitar o gerenciamento de pacientes, médicos e consultas, permitindo organizar os atendimentos de maneira simples.

## 2. Problema e solução

O gerenciamento manual de consultas pode causar problemas como conflitos de horários, dificuldade para localizar informações e falta de organização dos atendimentos.

Para solucionar esse problema, desenvolvemos um sistema que permite cadastrar pacientes e médicos, agendar consultas, consultar horários disponíveis, cancelar e remarcar atendimentos, além de consultar o histórico dos pacientes.

## 3. Funcionalidades

- Cadastro de pacientes.
- Cadastro de médicos e especialidades.
- Agendamento de consultas.
- Consulta de horários disponíveis.
- Cancelamento de consultas.
- Remarcação de consultas.
- Consulta do histórico de atendimentos.
- Diferenciação entre consultas presenciais e remotas.
- Verificação de conflitos de horários.

## 4. Paradigma de programação

O paradigma utilizado no projeto é a **Programação Orientada a Objetos (POO)**.

Esse paradigma organiza o programa por meio de classes e objetos, permitindo representar elementos do mundo real, como pacientes, médicos e atendimentos.

Os conceitos utilizados são:

- **Abstração:** a classe `Atendimento` representa as características comuns de uma consulta.
- **Encapsulamento:** atributos privados são utilizados nas classes `Paciente`, `Medico` e `Clinica`.
- **Herança:** as classes `ConsultaPresencial` e `ConsultaRemota` herdam características da classe `Atendimento`.
- **Polimorfismo:** cada tipo de consulta possui sua própria implementação do método `detalhes()`.
- **Relacionamento entre classes:** um atendimento está relacionado a um paciente e a um médico.

## 5. Linguagem e tecnologias

- Linguagem: Python.
- Interface gráfica: Tkinter.
- Paradigma: Programação Orientada a Objetos.

## 6. Organização dos arquivos

- `main.py`: inicia o sistema e carrega os dados de teste.
- `interface.py`: contém a interface gráfica e a interação com o usuário.
- `clinica.py`: gerencia os cadastros e os atendimentos.
- `paciente.py`: define a classe Paciente.
- `medico.py`: define a classe Medico.
- `atendimento.py`: define a classe abstrata Atendimento.
- `consulta_presencial.py`: define a consulta presencial.
- `consulta_remota.py`: define a consulta remota.

## 7. Como executar

1. Instale o Python.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

```bash
python main.py
```

Não é necessário instalar bibliotecas externas. A interface utiliza o Tkinter.

## 8. Dados de teste

O sistema inicia com pacientes, médicos e consultas previamente cadastrados para facilitar a demonstração das funcionalidades.

## 9. Integrantes

- [Nome do integrante 1]
- [Nome do integrante 2]
- [Nome do integrante 3]
- [Nome do integrante 4]

## 10. Disciplina

Paradigmas de Programação

**Professor:** [Nome do professor]

**Instituição:** [Nome da instituição]

**Ano:** 2026