import random
import string

def generar_contrasena(longitud):

    caracteres = string.ascii_letters + string.digits + string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():

    usuario = input("Introduce tu nombre de usuario: ")

    longitud = int(input("Introduce la longitud de la contraseña: "))

    if longitud >= 8:
        contrasena = generar_contrasena(longitud)
        print(f"Usuario: {usuario}")
        print(f"Tu contraseña generada es: {contrasena}")
    else:
        print("La longitud de la contraseña debe ser al menos 8 caracteres.")

if __name__ == "__main__":
    main()
