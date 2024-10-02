import os

import customtkinter as ctk
from PIL import Image, ImageTk

from .estilos import *


class ImageComponent(ctk.CTkFrame):
    def __init__(self, master, img_filename, size=(300, 300)):
        super().__init__(master, fg_color="transparent")

        # Obtém o caminho absoluto do arquivo atual
        self.dir_file = os.path.abspath(__file__)
        self.dir_path = os.path.dirname(self.dir_file)

        self.image_path = os.path.join(os.path.dirname(self.dir_path), "img", img_filename)

        self.image = Image.open(self.image_path)
        self.image = self.image.resize(size)
        self.logo_image = ImageTk.PhotoImage(self.image)

        self.label = ctk.CTkLabel(self, image=self.logo_image)
        self.label.pack()


class FrameComponent(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label= ctk.CTkLabel(self, text="Selecionar Robô")
        self.label.place(x=400, y=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
        self.title("Optimus")
        self.resizable(False, False)  # bloqueia o ajuste da tela pelo usuário

        self.image_component = ImageComponent(self, img_filename="logo_robot.png")
        self.image_component.pack(side="left", padx=10, pady=10)

        self.frame_component = FrameComponent(self, width=400, height=400)
        self.frame_component.pack(side="right", fill="y")








    