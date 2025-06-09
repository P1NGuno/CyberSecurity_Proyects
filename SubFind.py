

def main():
    dominio = input("Ingrese el dominio ")
    
    doc = open("hola.txt")

    print(doc.read() + "." + dominio)
    

if __name__ == "__main__":
    main()