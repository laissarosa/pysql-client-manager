from tkinter import *

class Gui:
    def __init__(self):
        self.x_pad = 15
        self.y_pad = 12
        self.width_entry = 50

        self.window = Tk()
        self.window.title("PYSQL")

        # Label de boas-vindas
        label = Label(self.window, text="Bem-vindo ao PYSQL")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Variáveis
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

        # Labels e Entradas
        Label(self.window, text="Nome").grid(row=1, column=0)
        Entry(self.window, textvariable=self.txtNome, width=self.width_entry).grid(row=1, column=1)

        Label(self.window, text="Sobrenome").grid(row=2, column=0)
        Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry).grid(row=2, column=1)

        Label(self.window, text="Email").grid(row=3, column=0)
        Entry(self.window, textvariable=self.txtEmail, width=self.width_entry).grid(row=3, column=1)

        Label(self.window, text="CPF").grid(row=4, column=0)
        Entry(self.window, textvariable=self.txtCPF, width=self.width_entry).grid(row=4, column=1)

        # Listbox + Scrollbar
        self.list_clients = Listbox(self.window, width=100)
        self.list_clients.grid(row=1, column=2, rowspan=10, sticky="NS")

        self.scroll_clients = Scrollbar(self.window)
        self.scroll_clients.grid(row=1, column=3, rowspan=10, sticky="NS")

        self.list_clients.configure(yscrollcommand=self.scroll_clients.set)
        self.scroll_clients.configure(command=self.list_clients.yview)

        # Botões
        Button(self.window, text="Ver todos").grid(row=5, column=0, columnspan=2, sticky="WE")
        Button(self.window, text="Buscar").grid(row=6, column=0, columnspan=2, sticky="WE")
        Button(self.window, text="Adicionar").grid(row=7, column=0, columnspan=2, sticky="WE")
        Button(self.window, text="Atualizar").grid(row=8, column=0, columnspan=2, sticky="WE")
        Button(self.window, text="Deletar").grid(row=9, column=0, columnspan=2, sticky="WE")
        Button(self.window, text="Fechar", command=self.window.destroy).grid(row=10, column=0, columnspan=2, sticky="WE")

    def run(self):
        self.window.mainloop()

