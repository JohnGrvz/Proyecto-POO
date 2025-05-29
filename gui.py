import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from Citas import Agenda
from Usuario import Usuario
from errores import FechaHoraInvalidaError
from tkinter import messagebox
import tkinter as tk
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
    def verify_login(self):
        """Verifica las credenciales de login"""
        user = self.user_entry.get()
        password = self.pass_entry.get()
        if usuario_app.verificar_credenciales(user, password):
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas. Intente de nuevo.")

    def clear_window(self):
        """Limpia la ventana actual"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        """Muestra el menú principal"""
        self.clear_window()
        self.root.title("Menú Principal - Consultorio Odontológico")

        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Menú Principal", font=("Helvetica", 18, "bold")).pack(pady=10)

        buttons = [
            ("Mostrar citas pendientes", self.show_pending_appointments),
            ("Agendar nueva cita", self.show_schedule_appointment),
            ("Mostrar citas con código", self.show_coded_appointments),
            ("Marcar cita como realizada", self.show_mark_appointment),
            ("Mostrar historias clínicas", self.show_clinical_histories),
            ("Editar historia clínica", self.show_edit_history),
            ("Mostrar historial de paciente", self.show_patient_history),
            ("Buscar cita por paciente", self.search_appointment),
            ("Cancelar cita", self.show_cancel_appointment),
            ("Exportar historial a PDF", self.show_export_pdf),
            ("Salir", self.exit_app)
        ]

        for text, command in buttons:
            ttkb.Button(frame, text=text, bootstyle=PRIMARY, command=command, width=30).pack(pady=5, fill='x')

    def show_pending_appointments(self):
        """Muestra las citas pendientes"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Citas Pendientes", font=("Helvetica", 16, "bold")).pack(pady=10)
        text_area = ttkb.Text(frame, height=15)
        text_area.pack(fill='both', expand=True, padx=10, pady=10)

        for cita in agenda.citas:
            if not cita.realizada:
                text_area.insert(tk.END, str(cita) + "\n")
        text_area.config(state='disabled')

        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=10)

    def show_schedule_appointment(self):
        """Muestra el formulario para agendar cita"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Agendar Nueva Cita", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttkb.Label(frame, text="Nombre del paciente:").pack(pady=5)
        paciente_entry = ttkb.Entry(frame)
        paciente_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        fecha_entry = ttkb.Entry(frame)
        fecha_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Hora (HH:MM AM/PM):").pack(pady=5)
        hora_entry = ttkb.Entry(frame)
        hora_entry.pack(pady=5, fill='x')

        def schedule():
            try:
                clave = agenda.agendar_cita(paciente_entry.get(), fecha_entry.get(), hora_entry.get())
                messagebox.showinfo("Éxito", f"Cita agendada con código: {clave}")
                self.show_main_menu()
            except FechaHoraInvalidaError as e:
                messagebox.showerror("Error de fecha/hora", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al agendar la cita: {str(e)}")
        ttkb.Button(frame, text="Agendar", bootstyle=SUCCESS, command=schedule).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

