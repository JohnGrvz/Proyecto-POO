from Paciente import Paciente
class Cita:
    contador_clave = 1

    def __init__(self, paciente, fecha, hora):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.realizada = False
        self.numero_clave = f"{Cita.contador_clave:03d}"
        Cita.contador_clave += 1

    def modificar_cita(self, nueva_fecha, nueva_hora):
        self.fecha = nueva_fecha
        self.hora = nueva_hora

    def cancelar_cita(self):
        self.fecha = None
        self.hora = None
        self.paciente = None

    def marcar_como_realizada(self, tratamiento, costo, pacientes_registrados):
        self.realizada = True
        if self.paciente not in pacientes_registrados:
            pacientes_registrados[self.paciente] = Paciente(self.paciente)
        pacientes_registrados[self.paciente].agregar_historia_clinica(tratamiento, costo, self.fecha)

    def __str__(self):
        estado = "Realizada" if self.realizada else "Pendiente"
        return f"Cita {self.numero_clave}: {self.paciente} - {self.fecha} a las {self.hora} ({estado})"
class Agenda:
    def __init__(self):
        self.citas = []
    def agendar_cita(self, paciente, fecha, hora):
        nueva_cita = Cita(paciente, fecha, hora)
        self.citas.append(nueva_cita)
        print(f"Cita agendada con éxito. Código de cita: {nueva_cita.numero_clave}\n")
    def listar_citas_pendientes(self):
        print("\nCitas pendientes:")
        for cita in self.citas:
            if not cita.realizada:
                print(cita)
    def buscar_cita(self, paciente):
        for cita in self.citas:
            if cita.paciente == paciente:
                return cita.numero_clave
        print("No se encontró una cita para ese paciente.")
        return None
    def cancelar_cita(self, clave):
        for cita in self.citas:
            if cita.numero_clave == clave:
                cita.cancelar_cita()
                print("Cita cancelada exitosamente.\n")
                return
        print("No se encontró una cita con ese código.\n")

