def main():
    try:
        long = int(input("Ingrese la longitud de la contraseña que desea. \nEsta debe ser mayor que 8 \n"))

        if long <= 8:
            print("La longitud debe de ser 8")
        else:
            print("Correcto")

    except ValueError as e:
        print(f"Error {e}")

if __name__ == "__main__":
    main()
