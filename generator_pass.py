def generator_pass (letras_min = True , letras_mayus = True, num = True , caract_espec = True):
    print(f"minusculas {letras_min} mayusculas {letras_mayus} num {num} caracteristicas especiales {caract_espec}")

def main():
    try:
        longitud = int(input("Longitud de la contraseña (mínimo 8): "))
        if longitud < 8:
            raise ValueError("La longitud mínima es 8.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    letras_min = input("Quiere ingresar letras minusculas?: s/n ").lower() == "s"
    letras_mayus = input("Quiere ingresar letras mayusculas?: s/n ").lower() == "s"
    num = input("Quiere ingresar numeros?: s/n ").lower() == "s"
    caract_espec = input("Quiere ingresar caracteres especiales?: s/n ").lower() == "s"
    generator_pass(letras_min, letras_mayus, num , caract_espec)

    

if __name__ == "__main__":
    main()
