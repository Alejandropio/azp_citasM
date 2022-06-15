import consultas.consulta as modelo

class Acciones:
    def agregar(self, doctor):
        print(f"\n [{doctor[6].upper()}] {doctor[1]} {doctor[2]}  - Agendar nueva consulta")

        nom_paciente = input("Introduce el nombre del paciente: ")
        genero = input("Introduce su genero (H/M): ")
        edad = input("Introduce su edad: ")
        telefono = input("Introduce su telefono: ")
        fecha_consulta = input("Introduce la fecha para hacer la consulta [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta)
        guardar = consulta.agregar()
        if guardar[0] >= 1:
            print(f"\nse ha hagendado: {consulta.nom_paciente} \n")
        else:
            print(f"\n error de al agendar {doctor[1]} ")
    
    def listar(self, doctor):
        print(f"\n [{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Detalles ")
        consulta = modelo.Consulta(doctor[0])
        consultas = consulta.listar()
            
        if consultas:
            for consulta in consultas:
                print(f"""
    Paciente: {consulta[2]}
    Genero: {consulta[3]}
    Edad: {consulta[4]}
    Telefono: {consulta[5]}
    Para el: {consulta[6]}
    Agendado el: {consulta[7]}
    -----------------------------------------""")
        else:
            print("\n No hay ninguna consulta ")

    def actualizar(self, doctor):
        print(f"\n [{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Modificar consulta ")

        nom_paciente = input("Introduce el nombre del paciente: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente)
        validar = consulta.validar()
        if validar[0] != 0:
            self.modificar(doctor, nom_paciente)
        else:
            print(f"\n No se encontró ninguna consulta  [{nom_paciente}] ")

    def modificar(self, doctor,nombre):
        print(f"\n [{doctor[6].upper()}] {doctor[1]} {doctor[2]} - editar los campos {nombre} ")

        nom_paciente = input("Introduce el nuevo nombre del paciente: ")
        genero = input("Introduce su genero (M/F): ")
        edad = input("Introduce su edad: ")
        telefono = input("Introduce su telefono: ")
        fecha_consulta = input("Introduce la fecha para hacer la consulta [yyyy-mm-dd]: ")

        consulta = modelo.Consulta(doctor[0], nom_paciente, genero, edad, telefono, fecha_consulta, nombre)
        guardar = consulta.actualizar()
        if guardar[0] >= 1:
            print(f"\nSe han modificado los datos : {consulta.nom_paciente}. \n")
        else:
            print(f"\n No se pudo modificar ")
    
    def eliminar(self, doctor):
        print(f"\n [{doctor[6].upper()}] {doctor[1]} {doctor[2]} - Borrar una consulta de la agenda ")
        nom_paciente = input("Introduce el nombre del paciente para eliminar : ")

        nota = modelo.Consulta(doctor[0], nom_paciente)
        eliminar = nota.eliminar()
        if eliminar[0] >= 1:
            print(f"\n Se eliminó la consulta : {nota.nom_paciente} ")
        else:
            print("\nNo se puedo eliminar la consulta")