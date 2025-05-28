from fpdf import FPDF

class HistoriaClinica:
    def __init__(self, nombre: str, tratamiento: str, costo: float, fecha: str):
        self.nombre = nombre
        self.tratamiento = tratamiento
        self.costo = costo
        self.fecha = fecha

    def __str__(self):
        return f"Paciente: {self.nombre}, Fecha: {self.fecha}, Tratamiento: {self.tratamiento}, Costo: ${self.costo:.2f}"
class Paciente:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.historial = []

    def agregar_historia_clinica(self, tratamiento: str, costo: float, fecha: str):
        historia = HistoriaClinica(self.nombre, tratamiento, costo, fecha)
        self.historial.append(historia)

    def editar_historia(self, fecha: str, nuevo_tratamiento: str, nuevo_costo: float):
        for historia in self.historial:
            if historia.fecha == fecha:
                historia.tratamiento = nuevo_tratamiento
                historia.costo = nuevo_costo
                print("Historia clínica actualizada.")
                return
        print("No se encontró una historia clínica con esa fecha.")

    def __str__(self):
        if not self.historial:
            return f"Paciente: {self.nombre} - No tiene historias clínicas registradas."
        historial_str = f"\nHistorial clínico del paciente {self.nombre}:\n"
        for historia in self.historial:
            historial_str += str(historia) + "\n"
        return historial_str

    def exportar_historial_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Historial clínico de {self.nombre}", ln=True, align='C')
        pdf.ln(10)
        for historia in self.historial:
            pdf.multi_cell(0, 10, txt=str(historia))
        archivo = f"{self.nombre}_historial.pdf"
        pdf.output(archivo)
        print(f"PDF exportado exitosamente: {archivo}")