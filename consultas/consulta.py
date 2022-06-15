import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Consulta:
    def __init__(self,id_doctor, nom_paciente="", genero="", edad=None, telefono="", fecha_consulta = None, nombre = ""):
        self.id_doctor = id_doctor
        self.nom_paciente = nom_paciente
        self.genero = genero
        self.edad = edad
        self.telefono = telefono
        self.fecha_consulta = fecha_consulta
        self.nombre = nombre

    def agregar(self):
        sql = "INSERT INTO consultas VALUES(null,%s, %s, %s, %s, %s, %s, NOW())"
        consulta = (self.id_doctor, self.nom_paciente, self.genero, self.edad, self.telefono, self.fecha_consulta)

        cursor.execute(sql, consulta)
        database.commit()
        return [cursor.rowcount, self]
    def listar(self):
        sql = f"SELECT * FROM consultas WHERE id_doctor = {self.id_doctor}"
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def validar(self):
        sql = f"SELECT * FROM consultas WHERE nom_paciente = '{self.nom_paciente}'"
        cursor.execute(sql)
        return [cursor.rowcount, self]
        
    def actualizar(self):
        sql = f"UPDATE consultas SET nom_paciente = '{self.nom_paciente}', telefono = '{self.telefono}', edad = {self.edad} WHERE nom_paciente = '{self.nombre}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]

    def eliminar(self):
        sql = f"DELETE FROM consultas WHERE id_doctor = {self.id_doctor} AND nom_paciente = '{self.nom_paciente}'"
        cursor.execute(sql)
        database.commit()
        return [cursor.rowcount, self]