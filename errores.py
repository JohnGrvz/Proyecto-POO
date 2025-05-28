class FechaHoraInvalidaError(Exception):
    """Se lanza cuando la fecha u hora ingresada para una cita no es válida."""
    def __init__(self, mensaje="Fecha u hora no válida. Asegúrese de que el formato y los valores sean correctos."):
        super().__init__(mensaje)
class FechaPasadaError(Exception):
    """Se lanza cuando se intenta agendar una cita en una fecha/hora que ya pasó."""
    pass
class CitaYaRealizadaError(Exception):
    """Se lanza cuando se intenta modificar o cancelar una cita ya realizada."""
    pass
class CamposObligatoriosVaciosError(Exception):
    """Se lanza cuando hay campos obligatorios vacíos al registrar o editar información."""
    pass