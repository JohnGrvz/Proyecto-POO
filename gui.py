import ttkbootstrap as ttkb
from Citas import Agenda
from Usuario import Usuario

pacientes_registrados = {}
agenda = Agenda()
usuario_app = Usuario()


class DentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Consultorio Odontológico")
        self.root.geometry("800x600")
        self.style = ttkb.Style(theme='flatly')  # Tema moderno
        self.show_login()