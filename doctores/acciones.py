import doctores.doctor as modelo
import consultas.acciones

class Acciones:
    def registro(self):

        print("\nIntroduzca sus datos para el registro en el sistema.")
        nombre = input("¿Cuál es su nombre?: ")
        apellidos = input("¿Cuáles son sus apellidos?: ")
        cedula = input("¿Cuáles son su cédula profesional?: ")
        especialidad = input("¿Cuál es su especialidad?: ")
        telefono = input("¿Cuál es su número de teléfono?: ")
        nconsultorio = input("¿Cuál es el nombre de su consultorio?: ")
        email = input("¿Cuál es su Email?: ")
        password = input("Introduzca su contraseña: ")

        doctor = modelo.Doctor(nombre, apellidos, cedula, especialidad, telefono, nconsultorio, email, password)
        registro = doctor.registrar()
        if registro[0] >= 1:
            print(f"\n Perfecto {registro[1].nombre} {registro[1].apellidos} se ha registrado  con el email {registro[1].email} ")
        else:
            print("\n Ha ocurrido un error, no se ha podido realizar su registro. Intente de nuevo más tarde.")

    def login(self):
        print("\nInicie sesión en el sistema")
        try:
            email = input("Introduzca su Email: ")
            password = input("Introduzca su contraseña: ")

            doctor = modelo.Doctor('','','','','', '',email, password)
            login = doctor.login()
            if email == login[7]:
                print(f"\n[{login[6].upper()}] Bienvenido {login[1]} {login[2]}, ha iniciado sesión en el sistema con el correo {login[7]}")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e)) - print(type(e).__name__)
            print("\nLogin incorrecto!! Intentalo más tarde")

    def proximasAcciones(self, doctor):
        print("""
Acciones disponibles:
    - Agendar consulta (1)
    - Listar consultas (2)
    - Modificar consulta (3)
    - Eliminar consulta (4)
    - Salir (5)
""")

        accion = input("¿Qué quiere hacer?: ")
        hazEl = consultas.acciones.Acciones()
        if accion == "1":
            hazEl.agregar(doctor)
            self.proximasAcciones(doctor) 
        elif accion == "2":
            hazEl.listar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "3":
            hazEl.actualizar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "4":
            hazEl.eliminar(doctor)
            self.proximasAcciones(doctor)
        elif accion == "5":
            print("\nVuelva Pronto!!!")
            exit()
        else:
            print("\n¡¡¡Acción invalida!!!")
            self.proximasAcciones(doctor)
