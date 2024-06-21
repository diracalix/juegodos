import string
import secrets


def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena


def main():
    try:
        longitud_deseada = int(
            input("Ingresa la longitud deseada (entre 8 y 16 caracteres): "))
        if 8 <= longitud_deseada <= 16:
            contrasena_segura = generar_contrasena(longitud_deseada)
            print(f"Contraseña segura generada: {contrasena_segura}")
        else:
            print("La longitud debe estar entre 8 y 16 caracteres.")
    except ValueError:
        print("Ingresa un número válido para la longitud.")


if __name__ == "__main__":
    main()
