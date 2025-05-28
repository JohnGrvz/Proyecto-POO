class FechaHoraInvalidaError(Exception):
    """Se lanza cuando la fecha u hora ingresada para una cita no es válida."""
    def __init__(self, mensaje="Fecha u hora no válida. Asegúrese de que el formato y los valores sean correctos."):
        super().__init__(mensaje)
