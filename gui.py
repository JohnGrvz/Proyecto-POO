import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

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

    def show_login(self):
        """Muestra la ventana de login"""
        self.clear_window()
        self.root.title("Iniciar Sesión - Consultorio Odontológico")

        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Bienvenido al Sistema Odontológico", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttkb.Label(frame, text="Usuario:").pack(pady=5)
        self.user_entry = ttkb.Entry(frame)
        self.user_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Contraseña:").pack(pady=5)
        self.pass_entry = ttkb.Entry(frame, show="*")
        self.pass_entry.pack(pady=5, fill='x')

        ttkb.Button(frame, text="Iniciar Sesión", bootstyle=SUCCESS, command=self.verify_login).pack(pady=20)