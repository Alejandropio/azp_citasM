import hashlib #Cifrar contraseñas en Python
import doctores.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Doctor:
    def __init__(self, nombre, apellidos, cedula, especialidad, telefono, nconsultorio, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.cedula = cedula
        self.telefono = telefono
        self.nconsultorio = nconsultorio
        self.especialidad = especialidad
        self.email = email
        self.password = password
    
    def registrar(self):
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))
        sql = "INSERT INTO doctors VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, NOW())"
        doctor = (self.nombre, self.apellidos, self.cedula, self.especialidad, self.telefono, self.nconsultorio, self.email, cifrado.hexdigest())

        try:
            cursor.execute(sql, doctor)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        return result
    
    def login(self):
        sql = "SELECT * FROM doctors WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256() # Cifrar contraseña
        cifrado.update(self.password.encode('utf8'))

        doctor = (self.email, cifrado.hexdigest())
        cursor.execute(sql, doctor)
        result = cursor.fetchone()
        return result