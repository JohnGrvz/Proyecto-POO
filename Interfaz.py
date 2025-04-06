from Citas import Agenda
from Paciente import Paciente
from Usuario import Usuario

# Diccionario de pacientes registrados
pacientes_registrados = {}

# Instancia de Agenda
agenda = Agenda()

# Usuario esperado
usuario_app = Usuario()

def login():
    print("\nBienvenido al sistema del consultorio odontológico")
    while True:
        user = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        if usuario_app.verificar_credenciales(user, password):
            print("\nInicio de sesión exitoso.\n")
            break
        else:
            print("Credenciales incorrectas. Intente de nuevo.\n")

def mostrar_menu():
    print("--- Menú principal ---")
    print("1. Mostrar las citas a realizar")
    print("2. Agendar una nueva cita")
    print("3. Mostrar citas a realizar (con código)")
    print("4. Marcar cita como realizada")
    print("5. Mostrar historias clínicas")
    print("6. Editar historias clínicas")
    print("7. Mostrar historial de un paciente")
    print("8. Buscar cita por paciente")
    print("9. Cancelar cita")
    print("0. Salir")

def main():
    login()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for cita in agenda.citas:
                if not cita.realizada:
                    print(cita)

        elif opcion == "2":
            paciente = input("Nombre del paciente: ")
            fecha = input("Fecha (YYYY-MM-DD): ")
            hora = input("Hora (HH:MM AM/PM): ")
            agenda.agendar_cita(paciente, fecha, hora)

        elif opcion == "3":
            agenda.listar_citas_pendientes()

        elif opcion == "4":
            codigo = input("Ingrese el código de la cita: ")
            tratamiento = input("Tratamiento realizado: ")
            costo = float(input("Costo del tratamiento: "))
            for cita in agenda.citas:
                if cita.numero_clave == codigo and not cita.realizada:
                    cita.marcar_como_realizada(tratamiento, costo, pacientes_registrados)
                    print("Cita marcada como realizada y historia clínica registrada.\n")
                    break
            else:
                print("No se encontró una cita pendiente con ese código.\n")

        elif opcion == "5":
            for paciente in pacientes_registrados.values():
                print(paciente)

        elif opcion == "6":
            nombre = input("Nombre del paciente: ")
            fecha = input("Fecha de la historia a editar (YYYY-MM-DD): ")
            nuevo_tratamiento = input("Nuevo tratamiento: ")
            nuevo_costo = float(input("Nuevo costo: "))
            if nombre in pacientes_registrados:
                pacientes_registrados[nombre].editar_historia(fecha, nuevo_tratamiento, nuevo_costo)
            else:
                print("Paciente no encontrado.\n")

        elif opcion == "7":
            nombre = input("Nombre del paciente: ")
            if nombre in pacientes_registrados:
                print(pacientes_registrados[nombre])
            else:
                print("Paciente no encontrado.\n")

        elif opcion == "8":
            nombre = input("Nombre del paciente para buscar cita: ")
            clave = agenda.buscar_cita(nombre)
            if clave:
                print(f"Código de la cita: {clave}")

        elif opcion == "9":
            codigo = input("Ingrese el código de la cita a cancelar: ")
            agenda.cancelar_cita(codigo)

        elif opcion == "0":
            print("Saliendo del sistema... ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()
