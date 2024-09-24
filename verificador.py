import re

# Funcion para verificar minusculas
def verificar_minusculas(contraseña):
    return bool(re.search(r'[a-z]', contraseña))

# Funcion para verificar mayusculas
def verificar_mayusculas(contraseña):
    return bool(re.search(r'[A-Z]', contraseña))

# Función para verificar numeros
def verificar_numeros(contraseña):
    return bool(re.search(r'[1-9]', contraseña))

# Funcion para verificar si la contraseña tiene mas de 8 caracteres
def verificar_longitud(contraseña):
    return len(contraseña) > 8

