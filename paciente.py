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
                return True  # Indica que la historia fue editada exitosamente
        return False  # No se encontró una historia con esa fecha

    def obtener_historial_como_texto(self):
        if not self.historial:
            return f"Paciente: {self.nombre} - No tiene historias clínicas registradas."
        historial_str = f"\nHistorial clínico del paciente {self.nombre}:\n"
        for historia in self.historial:
            historial_str += str(historia) + "\n"
        return historial_str

    def exportar_historial_pdf(self):
        if not self.historial:
            return None

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Historial clínico de {self.nombre}", ln=True, align='C')
        pdf.ln(10)

        for historia in self.historial:
            pdf.set_font("Arial", 'B', 12)
            pdf.cell(0, 10, txt="Cita registrada:", ln=True)
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, txt=f"Fecha: {historia.fecha}", ln=True)
            pdf.cell(0, 10, txt=f"Tratamiento: {historia.tratamiento}", ln=True)
            pdf.cell(0, 10, txt=f"Costo: ${historia.costo:.2f}", ln=True)
            pdf.ln(5)
            pdf.cell(0, 5, txt="----------------------------", ln=True)
            pdf.ln(5)

        archivo = f"{self.nombre}_historial.pdf"
        pdf.output(archivo)
        return archivo
