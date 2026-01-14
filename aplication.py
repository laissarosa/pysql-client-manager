from frontend import Gui
from tkinter import *
import backend as core

class Application(Gui):
    def __init__(self):
        super().__init__() 
        self.btn_view_all = self._create_button("Ver todos", self.view_all, row=5)
        self.btn_search = self._create_button("Buscar", self.search_client, row=6)
        self.btn_add = self._create_button("Adicionar", self.add_client, row=7)
        self.btn_update = self._create_button("Atualizar", self.update_client, row=8)
        self.btn_delete = self._create_button("Deletar", self.delete_client, row=9)
        self.btn_close = self._create_button("Fechar", self.window.destroy, row=10)

    def _create_button(self, text, command, row):
        btn = Button(self.window, text=text, command=command)
        btn.grid(row=row, column=0, columnspan=2, sticky="WE", padx=self.x_pad, pady=self.y_pad)
        return btn

    def view_all(self):
        self.list_clients.delete(0, END)
        rows = core.view()
        for row in rows:
            self.list_clients.insert(END, row)

    def search_client(self):
        self.list_clients.delete(0, END)
        rows = core.search(
            self.txtNome.get(),
            self.txtSobrenome.get(),
            self.txtEmail.get(),
            self.txtCPF.get()
        )
        for row in rows:
            self.list_clients.insert(END, row)

    def add_client(self):
        core.insert(
            self.txtNome.get(),
            self.txtSobrenome.get(),
            self.txtEmail.get(),
            self.txtCPF.get()
        )
        self.view_all() 

    def update_client(self):
        try:
            selected = self.list_clients.get(self.list_clients.curselection())
            core.update(selected[3], self.txtNome.get(), self.txtSobrenome.get(), self.txtEmail.get(), self.txtCPF.get())
            self.view_all()
        except:
            pass

    def delete_client(self):
        try:
            selected = self.list_clients.get(self.list_clients.curselection())
            core.delete(selected[3])
            self.view_all()
        except:
            pass


if __name__ == "__main__":
    app = Application()
    app.run()