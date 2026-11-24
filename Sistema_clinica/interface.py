
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime


class Interface:
    def __init__(self, clinica):
        self.clinica = clinica
        self.janela = tk.Tk()
        self.janela.title("Sistema de Clínica")
        self.janela.geometry("950x650")
        self.janela.minsize(800, 550)
        self.janela.configure(bg="#eef2f8")

        self.configurar_estilo()
        self.criar_cabecalho()

        abas = ttk.Notebook(self.janela)
        abas.pack(fill="both", expand=True, padx=18, pady=12)

        self.pacientes = ttk.Frame(abas, padding=18)
        self.medicos = ttk.Frame(abas, padding=18)
        self.agendamentos = ttk.Frame(abas, padding=18)
        self.horarios = ttk.Frame(abas, padding=18)
        self.historico = ttk.Frame(abas, padding=18)

        for frame, nome in [
            (self.pacientes, "♙  Pacientes"),
            (self.medicos, "✚  Médicos"),
            (self.agendamentos, "▣  Agendamentos"),
            (self.horarios, "◷  Horários"),
            (self.historico, "▤  Histórico")
        ]:
            abas.add(frame, text=nome)

        self.criar_pacientes()
        self.criar_medicos()
        self.criar_agendamentos()
        self.criar_horarios()
        self.criar_historico()
        self.criar_rodape()

    def configurar_estilo(self):
        estilo = ttk.Style()
        estilo.theme_use("clam")

        estilo.configure(
            "TNotebook",
            background="#eef2f8",
            borderwidth=0
        )

        estilo.configure(
            "TNotebook.Tab",
            background="#dce5f1",
            foreground="#34445c",
            padding=(15, 11),
            font=("Segoe UI", 10, "bold")
        )

        estilo.map(
            "TNotebook.Tab",
            background=[("selected", "#ffffff")],
            foreground=[("selected", "#1676b8")]
        )

        estilo.configure(
            "TFrame",
            background="#ffffff"
        )

        estilo.configure(
            "TLabel",
            background="#ffffff",
            foreground="#34445c",
            font=("Segoe UI", 10)
        )

        estilo.configure(
            "TButton",
            background="#2878b5",
            foreground="#ffffff",
            padding=(12, 8),
            font=("Segoe UI", 9, "bold"),
            borderwidth=0
        )

        estilo.map(
            "TButton",
            background=[
                ("active", "#185f96"),
                ("disabled", "#aab8c8")
            ]
        )

        estilo.configure("TEntry", padding=7)
        estilo.configure("TCombobox", padding=7)

        estilo.configure(
            "Treeview",
            background="#ffffff",
            foreground="#34445c",
            rowheight=32,
            font=("Segoe UI", 9),
            fieldbackground="#ffffff"
        )

        estilo.configure(
            "Treeview.Heading",
            background="#e5edf7",
            foreground="#243b64",
            font=("Segoe UI", 9, "bold"),
            padding=9
        )

        estilo.map(
            "Treeview",
            background=[("selected", "#c9def5")],
            foreground=[("selected", "#243b64")]
        )

    def criar_cabecalho(self):
        topo = tk.Frame(self.janela, bg="#203b63", height=95)
        topo.pack(fill="x")
        topo.pack_propagate(False)

        faixa = tk.Frame(topo, bg="#36a3d9", width=7)
        faixa.pack(side="left", fill="y")

        conteudo = tk.Frame(topo, bg="#203b63")
        conteudo.pack(side="left", padx=22, pady=13)

        tk.Label(
            conteudo,
            text="Sistema de Clínica",
            font=("Segoe UI", 21, "bold"),
            bg="#203b63",
            fg="#ffffff"
        ).pack(anchor="w")

        tk.Label(
            conteudo,
            text="Gerenciamento de pacientes e consultas",
            font=("Segoe UI", 10),
            bg="#203b63",
            fg="#c6d8ed"
        ).pack(anchor="w", pady=(2, 0))

        tk.Label(
            topo,
            text="SAÚDE  •  ORGANIZAÇÃO  •  CUIDADO",
            font=("Segoe UI", 9, "bold"),
            bg="#203b63",
            fg="#8ecff0"
        ).pack(side="right", padx=22)

    def criar_rodape(self):
        rodape = tk.Frame(self.janela, bg="#eef2f8")
        rodape.pack(fill="x", padx=20, pady=(0, 8))

        tk.Label(
            rodape,
            text="Sistema de gerenciamento de clínica",
            font=("Segoe UI", 8),
            bg="#eef2f8",
            fg="#8290a3"
        ).pack(side="left")

        tk.Label(
            rodape,
            text="Versão 1.0",
            font=("Segoe UI", 8),
            bg="#eef2f8",
            fg="#8290a3"
        ).pack(side="right")

    def titulo(self, frame, texto):
        tk.Label(
            frame,
            text=texto,
            font=("Segoe UI", 15, "bold"),
            bg="#ffffff",
            fg="#243b64"
        ).pack(anchor="w", pady=(0, 12))

    def campo(self, frame, nome):
        linha = ttk.Frame(frame)
        linha.pack(fill="x", pady=4)

        ttk.Label(linha, text=nome, width=22).pack(side="left")

        entrada = ttk.Entry(linha)
        entrada.pack(side="left", fill="x", expand=True)

        return entrada

    def tabela(self, frame, colunas):
        tabela = ttk.Treeview(
            frame,
            columns=colunas,
            show="headings"
        )

        for coluna in colunas:
            tabela.heading(coluna, text=coluna)
            tabela.column(coluna, width=130, anchor="center")

        tabela.tag_configure("par", background="#f3f7fc")
        tabela.tag_configure("impar", background="#ffffff")
        tabela.tag_configure("Agendado", foreground="#16804a")
        tabela.tag_configure("Cancelado", foreground="#c0392b")

        tabela.pack(fill="both", expand=True, pady=12)

        return tabela

    def executar(self, funcao):
        try:
            funcao()
            self.atualizar()
        except ValueError as erro:
            messagebox.showerror("Atenção", str(erro))

    def criar_pacientes(self):
        f = self.pacientes
        self.titulo(f, "Cadastro de pacientes")

        self.p_nome = self.campo(f, "Nome")
        self.p_cpf = self.campo(f, "CPF")
        self.p_telefone = self.campo(f, "Telefone")

        ttk.Button(
            f,
            text="＋  Cadastrar paciente",
            command=lambda: self.executar(self.cadastrar_paciente)
        ).pack(anchor="e", pady=10)

        self.t_pacientes = self.tabela(
            f, ("Nome", "CPF", "Telefone")
        )

    def cadastrar_paciente(self):
        self.clinica.cadastrar_paciente(
            self.p_nome.get(),
            self.p_cpf.get(),
            self.p_telefone.get()
        )
        messagebox.showinfo("Sucesso", "Paciente cadastrado!")

    def criar_medicos(self):
        f = self.medicos
        self.titulo(f, "Cadastro de médicos")

        self.m_nome = self.campo(f, "Nome")
        self.m_crm = self.campo(f, "CRM")
        self.m_especialidade = self.campo(f, "Especialidade")

        ttk.Button(
            f,
            text="＋  Cadastrar médico",
            command=lambda: self.executar(self.cadastrar_medico)
        ).pack(anchor="e", pady=10)

        self.t_medicos = self.tabela(
            f, ("Nome", "CRM", "Especialidade")
        )

    def cadastrar_medico(self):
        self.clinica.cadastrar_medico(
            self.m_nome.get(),
            self.m_crm.get(),
            self.m_especialidade.get()
        )
        messagebox.showinfo("Sucesso", "Médico cadastrado!")

    def criar_agendamentos(self):
        f = self.agendamentos
        self.titulo(f, "Gerenciamento de consultas")

        self.a_cpf = self.campo(f, "CPF do paciente")
        self.a_crm = self.campo(f, "CRM do médico")
        self.a_data = self.campo(
            f, "Data e hora (dd/mm/aaaa hh:mm)"
        )

        linha = ttk.Frame(f)
        linha.pack(fill="x", pady=4)

        ttk.Label(linha, text="Tipo de consulta", width=22).pack(side="left")

        self.a_tipo = ttk.Combobox(
            linha,
            values=["Presencial", "Remota"],
            state="readonly"
        )
        self.a_tipo.pack(side="left", fill="x", expand=True)
        self.a_tipo.set("Presencial")

        self.a_detalhe = self.campo(f, "Sala ou link")

        ttk.Button(
            f,
            text="＋  Agendar consulta",
            command=lambda: self.executar(self.agendar)
        ).pack(anchor="e", pady=10)

        self.t_agendamentos = self.tabela(
            f,
            ("Paciente", "Médico", "Data", "Tipo", "Detalhe", "Status")
        )

        botoes = ttk.Frame(f)
        botoes.pack(pady=5)

        ttk.Button(
            botoes,
            text="Cancelar consulta",
            command=lambda: self.executar(self.cancelar)
        ).pack(side="left", padx=5)

        ttk.Button(
            botoes,
            text="Remarcar consulta",
            command=lambda: self.executar(self.remarcar)
        ).pack(side="left", padx=5)

    def agendar(self):
        data = datetime.strptime(
            self.a_data.get(), "%d/%m/%Y %H:%M"
        )

        self.clinica.agendar(
            self.a_cpf.get(),
            self.a_crm.get(),
            data,
            self.a_tipo.get(),
            self.a_detalhe.get()
        )

        messagebox.showinfo("Sucesso", "Consulta agendada!")

    def atendimento_selecionado(self):
        selecao = self.t_agendamentos.selection()

        if not selecao:
            raise ValueError("Selecione um atendimento.")

        indice = int(selecao[0])
        return self.clinica.listar_atendimentos()[indice]

    def cancelar(self):
        self.clinica.cancelar(self.atendimento_selecionado())
        messagebox.showinfo("Sucesso", "Consulta cancelada!")

    def remarcar(self):
        atendimento = self.atendimento_selecionado()

        nova_data = simpledialog.askstring(
            "Remarcar consulta",
            "Nova data e hora (dd/mm/aaaa hh:mm):"
        )

        if nova_data:
            data = datetime.strptime(
                nova_data, "%d/%m/%Y %H:%M"
            )
            self.clinica.remarcar(atendimento, data)
            messagebox.showinfo("Sucesso", "Consulta remarcada!")

    def criar_horarios(self):
        f = self.horarios
        self.titulo(f, "Consulta de horários disponíveis")

        self.h_crm = self.campo(f, "CRM do médico")
        self.h_data = self.campo(f, "Data (dd/mm/aaaa)")

        ttk.Button(
            f,
            text="⌕  Consultar horários",
            command=lambda: self.executar(self.consultar_horarios)
        ).pack(anchor="e", pady=10)

        self.lista_horarios = tk.Listbox(
            f,
            font=("Segoe UI", 11),
            bg="#f3f7fc",
            fg="#34445c",
            selectbackground="#2878b5",
            selectforeground="#ffffff",
            relief="flat",
            height=12,
            highlightthickness=1,
            highlightbackground="#dce5f1"
        )

        self.lista_horarios.pack(
            fill="both", expand=True, pady=12
        )

    def consultar_horarios(self):
        data = datetime.strptime(
            self.h_data.get(), "%d/%m/%Y"
        ).date()

        horarios = self.clinica.consultar_horarios(
            self.h_crm.get(), data
        )

        self.lista_horarios.delete(0, tk.END)

        for horario in horarios:
            self.lista_horarios.insert(
                tk.END, "   " + horario.strftime("%H:%M")
            )

        if not horarios:
            self.lista_horarios.insert(
                tk.END, "Nenhum horário disponível."
            )

    def criar_historico(self):
        f = self.historico
        self.titulo(f, "Histórico de atendimentos")

        self.h_cpf = self.campo(f, "CPF do paciente")

        ttk.Button(
            f,
            text="⌕  Consultar histórico",
            command=lambda: self.executar(self.consultar_historico)
        ).pack(anchor="e", pady=10)

        self.t_historico = self.tabela(
            f, ("Médico", "Data", "Tipo", "Detalhe", "Status")
        )

    def consultar_historico(self):
        atendimentos = self.clinica.historico(
            self.h_cpf.get()
        )

        for item in self.t_historico.get_children():
            self.t_historico.delete(item)

        for i, a in enumerate(atendimentos):
            self.t_historico.insert(
                "",
                "end",
                values=(
                    a.medico.nome,
                    a.data_hora.strftime("%d/%m/%Y %H:%M"),
                    type(a).__name__.replace("Consulta", ""),
                    a.detalhes(),
                    a.status
                ),
                tags=("par" if i % 2 == 0 else "impar", a.status)
            )

    def atualizar(self):
        for tabela in (
            self.t_pacientes,
            self.t_medicos,
            self.t_agendamentos
        ):
            for item in tabela.get_children():
                tabela.delete(item)

        for i, p in enumerate(self.clinica.listar_pacientes()):
            self.t_pacientes.insert(
                "",
                "end",
                values=(p.nome, p.cpf, p.telefone),
                tags=("par" if i % 2 == 0 else "impar",)
            )

        for i, m in enumerate(self.clinica.listar_medicos()):
            self.t_medicos.insert(
                "",
                "end",
                values=(m.nome, m.crm, m.especialidade),
                tags=("par" if i % 2 == 0 else "impar",)
            )

        for i, a in enumerate(self.clinica.listar_atendimentos()):
            self.t_agendamentos.insert(
                "",
                "end",
                iid=str(i),
                values=(
                    a.paciente.nome,
                    a.medico.nome,
                    a.data_hora.strftime("%d/%m/%Y %H:%M"),
                    type(a).__name__.replace("Consulta", ""),
                    a.detalhes(),
                    a.status
                ),
                tags=("par" if i % 2 == 0 else "impar", a.status)
            )

    def iniciar(self):
        self.janela.mainloop()
