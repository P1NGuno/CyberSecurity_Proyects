import random
import string

def generar_contraseña(longitud=12, usar_mayusculas=True, usar_minusculas=True, usar_numeros=True, usar_especiales=True):
    caracteres = ''
    
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de carácter.")

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("Generador de Contraseñas Seguras")
    
    try:
        longitud = int(input("Longitud de la contraseña (mínimo 4): "))
        if longitud < 4:
            raise ValueError("La longitud mínima es 4.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    usar_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
    usar_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    usar_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'

    try:
        contraseña = generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_especiales)
        print(f"\nTu nueva contraseña segura es:\n{contraseña}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
