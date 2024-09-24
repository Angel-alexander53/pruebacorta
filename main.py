from verificador import verificar_minusculas, verificar_mayusculas, verificar_numeros, verificar_longitud

def evaluar_contraseña(contraseña):
    contador = 0  # Variable contador inicializada en 0

    # Lista de verificaciones
    verificaciones = []

    # Verificacion de cada uno de los criterios
    if verificar_minusculas(contraseña):
        verificaciones.append("Contiene letras minusculas")
        contador += 25

    if verificar_mayusculas(contraseña):
        verificaciones.append("Contiene letras mayusculas")
        contador += 25

    if verificar_numeros(contraseña):
        verificaciones.append("Contiene numeros del 1 al 9")
        contador += 25

    if verificar_longitud(contraseña):
        verificaciones.append("Tiene mas de 8 caracteres")
        contador += 25

    # Mostrar resultados
    print("Verificaciones completadas:")
    for verificacion in verificaciones:
        print(f"- {verificacion}")

    # Mostrar el nivel de seguridad
    print(f"Nivel de seguridad de la contraseña: {contador}%")

# Solicitar contraseña al usuario
if __name__ == "__main__":
    contraseña = input("Introduce la contraseña: ")
    evaluar_contraseña(contraseña)
