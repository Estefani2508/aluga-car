import customtkinter as ctk

class ExibirVeiculos(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title('Visualização de Veiculos')
        self.geometry('800x600n')
        self.resizable(False, False)

        self.label_visualizar = ctk.CTkLabel(text="Janela Visualizar")
        self.label_visualizar.pack()