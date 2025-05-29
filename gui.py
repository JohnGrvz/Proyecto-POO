import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from Citas import Agenda
from Usuario import Usuario
from errores import CamposObligatoriosVaciosError, FechaHoraInvalidaError
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
        self.style = ttkb.Style(theme='flatly')
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

    def show_coded_appointments(self):
        """Muestra las citas con codigo"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Citas Pendientes con Código", font=("Helvetica", 16, "bold")).pack(pady=10)
        text_area = ttkb.Text(frame, height=15)
        text_area.pack(fill='both', expand=True, padx=10, pady=10)

        for cita in agenda.listar_citas_pendientes():
            text_area.insert(tk.END, cita + "\n")
        text_area.config(state='disabled')

        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=10)

    def show_mark_appointment(self):
        """Muestra el formulario para marcar cita como realizada"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Marcar Cita como Realizada", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttkb.Label(frame, text="Código de la cita:").pack(pady=5)
        codigo_entry = ttkb.Entry(frame)
        codigo_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Tratamiento realizado:").pack(pady=5)
        tratamiento_entry = ttkb.Entry(frame)
        tratamiento_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Costo del tratamiento:").pack(pady=5)
        costo_entry = ttkb.Entry(frame)
        costo_entry.pack(pady=5, fill='x')

        def mark():
            try:
                codigo = codigo_entry.get().strip()
                tratamiento = tratamiento_entry.get().strip()
                costo_texto = costo_entry.get().strip()

                if not codigo or not tratamiento or not costo_texto:
                    raise CamposObligatoriosVaciosError("Todos los campos son obligatorios.")

                try:
                    costo = float(costo_texto)
                except ValueError:
                    raise ValueError("El costo debe ser un número válido.")

                for cita in agenda.citas:
                    if cita.numero_clave == codigo:
                        if cita.realizada:
                            raise ValueError("La cita ya fue marcada como realizada.")
                        cita.marcar_como_realizada(tratamiento, costo, pacientes_registrados)
                        messagebox.showinfo("Éxito", "Cita marcada como realizada y historia clínica registrada.")
                        self.show_main_menu()
                        return

                raise ValueError("No se encontró una cita pendiente con ese código.")

            except (CamposObligatoriosVaciosError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Marcar Realizada", bootstyle=SUCCESS, command=mark).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def show_clinical_histories(self):
        """Muestra todas las historias clínicas"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Historias Clínicas", font=("Helvetica", 16, "bold")).pack(pady=10)
        text_area = ttkb.Text(frame, height=15)
        text_area.pack(fill='both', expand=True, padx=10, pady=10)

        if not pacientes_registrados:
            text_area.insert(tk.END, "No hay registros\n")
        else:
            for paciente in pacientes_registrados.values():
                text_area.insert(tk.END, paciente.obtener_historial_como_texto() + "\n")
        text_area.config(state='disabled')

        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=10)

    def show_edit_history(self):
        """Muestra el formulario para editar historia clínica"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Editar Historia Clínica", font=("Helvetica", 16, "bold")).pack(pady=10)

        ttkb.Label(frame, text="Nombre del paciente:").pack(pady=5)
        nombre_entry = ttkb.Entry(frame)
        nombre_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        fecha_entry = ttkb.Entry(frame)
        fecha_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Nuevo tratamiento:").pack(pady=5)
        tratamiento_entry = ttkb.Entry(frame)
        tratamiento_entry.pack(pady=5, fill='x')

        ttkb.Label(frame, text="Nuevo costo:").pack(pady=5)
        costo_entry = ttkb.Entry(frame)
        costo_entry.pack(pady=5, fill='x')

        def edit():
            try:
                nombre = nombre_entry.get().strip()
                fecha = fecha_entry.get().strip()
                nuevo_tratamiento = tratamiento_entry.get().strip()
                costo_texto = costo_entry.get().strip()

                if not nombre or not fecha or not nuevo_tratamiento or not costo_texto:
                    raise CamposObligatoriosVaciosError("Todos los campos son obligatorios.")

                try:
                    nuevo_costo = float(costo_texto)
                except ValueError:
                    raise ValueError("El costo debe ser un número válido.")

                if nombre not in pacientes_registrados:
                    raise ValueError("Paciente no encontrado.")

                exito = pacientes_registrados[nombre].editar_historia(fecha, nuevo_tratamiento, nuevo_costo)
                if not exito:
                    raise FechaHoraInvalidaError("No se encontró una historia con esa fecha.")

                messagebox.showinfo("Éxito", "Historia clínica editada correctamente.")
                self.show_main_menu()

            except (CamposObligatoriosVaciosError, FechaHoraInvalidaError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Editar", bootstyle=SUCCESS, command=edit).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def show_patient_history(self):
        """Muestra el historial de un paciente"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Historial de Paciente", font=("Helvetica", 16, "bold")).pack(pady=10)
        ttkb.Label(frame, text="Nombre del paciente:").pack(pady=5)
        nombre_entry = ttkb.Entry(frame)
        nombre_entry.pack(pady=5, fill='x')

        def show():
            try:
                nombre = nombre_entry.get().strip()

                if not nombre:
                    raise CamposObligatoriosVaciosError("Debe ingresar el nombre del paciente.")

                if nombre not in pacientes_registrados:
                    raise ValueError("Paciente no encontrado.")

                self.clear_window()
                frame = ttkb.Frame(self.root, padding=20)
                frame.pack(expand=True, fill='both')
                ttkb.Label(frame, text=f"Historial de {nombre}", font=("Helvetica", 16, "bold")).pack(pady=10)
                text_area = ttkb.Text(frame, height=15)
                text_area.pack(fill='both', expand=True, padx=10, pady=10)
                text_area.insert(tk.END, pacientes_registrados[nombre].obtener_historial_como_texto())
                text_area.config(state='disabled')
                ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=10)

            except (CamposObligatoriosVaciosError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Mostrar", bootstyle=SUCCESS, command=show).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def search_appointment(self):
        """Busca cita por nombre de paciente"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Buscar Cita por Paciente", font=("Helvetica", 16, "bold")).pack(pady=10)
        ttkb.Label(frame, text="Nombre del paciente:").pack(pady=5)
        nombre_entry = ttkb.Entry(frame)
        nombre_entry.pack(pady=5, fill='x')

        def search():
            try:
                nombre = nombre_entry.get().strip()

                if not nombre:
                    raise CamposObligatoriosVaciosError("Debe ingresar el nombre del paciente.")

                clave = agenda.buscar_cita(nombre)

                if clave:
                    messagebox.showinfo("Resultado", f"Código de la cita: {clave}")
                else:
                    raise ValueError("No se encontró una cita para ese paciente.")

            except (CamposObligatoriosVaciosError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Buscar", bootstyle=SUCCESS, command=search).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def show_cancel_appointment(self):
        """Muestra el formulario para cancelar cita"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Cancelar Cita", font=("Helvetica", 16, "bold")).pack(pady=10)
        ttkb.Label(frame, text="Código de la cita:").pack(pady=5)
        codigo_entry = ttkb.Entry(frame)
        codigo_entry.pack(pady=5, fill='x')

        def cancel():
            try:
                codigo = codigo_entry.get().strip()

                if not codigo:
                    raise CamposObligatoriosVaciosError("Debe ingresar el código de la cita.")

                if agenda.cancelar_cita(codigo):
                    messagebox.showinfo("Éxito", "Cita cancelada.")
                    self.show_main_menu()
                else:
                    raise ValueError("No se encontró una cita con ese código.")

            except (CamposObligatoriosVaciosError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Cancelar", bootstyle=DANGER, command=cancel).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def show_export_pdf(self):
        """Muestra el formulario para exportar historial a PDF"""
        self.clear_window()
        frame = ttkb.Frame(self.root, padding=20)
        frame.pack(expand=True, fill='both')

        ttkb.Label(frame, text="Exportar Historial a PDF", font=("Helvetica", 16, "bold")).pack(pady=10)
        ttkb.Label(frame, text="Nombre del paciente:").pack(pady=5)
        nombre_entry = ttkb.Entry(frame)
        nombre_entry.pack(pady=5, fill='x')

        def export():
            try:
                nombre = nombre_entry.get().strip()

                if not nombre:
                    raise CamposObligatoriosVaciosError("Debe ingresar el nombre del paciente.")

                if nombre not in pacientes_registrados:
                    raise ValueError("Paciente no encontrado.")

                archivo = pacientes_registrados[nombre].exportar_historial_pdf()

                if archivo:
                    messagebox.showinfo("Éxito", f"Historial exportado como {archivo}")
                    self.show_main_menu()
                else:
                    raise ValueError("No hay historial para exportar.")

            except (CamposObligatoriosVaciosError, ValueError) as e:
                messagebox.showerror("Error", str(e))

        ttkb.Button(frame, text="Exportar", bootstyle=SUCCESS, command=export).pack(pady=10)
        ttkb.Button(frame, text="Volver", bootstyle=SECONDARY, command=self.show_main_menu).pack(pady=5)

    def exit_app(self):
        """Cierra la aplicación"""
        messagebox.showinfo("Saliendo", "¡Hasta luego!")
        self.root.destroy()

if __name__ == "__main__":
    root = ttkb.Window()
    app = DentalApp(root)
    root.mainloop()