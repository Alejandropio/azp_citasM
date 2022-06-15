from doctores import acciones

print("""
Seleccione una acción:
    - Registro (1)
    - Login (2)
    - Salir (3)
""")
hazEl = acciones.Acciones()

accion = input("¿Qué quiere hacer?: ")
if accion == "1":
    hazEl.registro()
elif accion == "2":
    hazEl.login()
elif accion == "3":
    print("\nAdios.")
