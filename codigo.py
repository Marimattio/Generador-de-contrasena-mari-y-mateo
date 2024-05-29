import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

def main():
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    if longitud < 8:
        print("La longitud de la contraseña debe ser al menos 8 caracteres.")
    else:
        contrasena = generar_contrasena(longitud)
        print("Tu contraseña segura es:", contrasena)

if __name__ == "__main__":
    main()
