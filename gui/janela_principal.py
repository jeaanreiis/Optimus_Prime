import customtkinter as ctk
from .estilos import *

class JanelaPrincipal(ctk.CTk):  # Substitua tk.Tk por ctk.CTk
    def __init__(self):
        super().__init__()
        self.title("Gerenciador de Tarefas")
        self.geometry("600x400")

        # Criar os elementos da interface
        self.label = ctk.CTkLabel(self, text="Selecione um robô:", font=(FONTE_PRINCIPAL), text_color=COR_FONTE)
        self.combobox = ctk.CTkComboBox(self, values=["Robo 1", "Robo 2", "Robo 3"])
        self.button = ctk.CTkButton(self, text="Executar", command=self.bot_selecionado)
        
        # Posicionar os elementos na janela
        self.label.pack(pady=10)
        self.combobox.pack(pady=5)
        self.button.pack(pady=20)


    def bot_selecionado(self):
        print(f"Robô Selecionado: {self.combobox.get()}")  # TODO: remover linha no futuro 
        self.button.configure(text="Executando...")
        self.after(3000, self.botao_finalizado)


    def botao_finalizado(self):
        self.button.configure(text="Executar")  # Restaura o texto do botão



    