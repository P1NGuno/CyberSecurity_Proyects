
import string

def simpli_frase():
    frase_simpl = ''
    frase = input("Introduzca la palabra que quiera\n").lower()

    for letra in frase:
        if letra.isalpha():
            frase_simpl += letra

    return frase_simpl

def code_cesar(palabra, desplazamiento=3):
    abecedario = string.ascii_lowercase
    code_word = ''

    for letra_palabra in palabra:
        
        if letra_palabra in abecedario:
            
            posicion_original = abecedario.index(letra_palabra)

            
            posicion_cifrada = (posicion_original + desplazamiento) % 26

            
            letra_cifrada = abecedario[posicion_cifrada]

            code_word += letra_cifrada
        else:
            
            code_word += letra_palabra

    return code_word

def decode_cesar(palabra, desplazamiento = 3):
    abecedario = string.ascii_lowercase
    decode_word = ''

    for letra_palabra in palabra:

        if letra_palabra in abecedario :
            posicion_original = abecedario.index(letra_palabra)

            
            posicion_cifrada = (posicion_original - desplazamiento) % 26
 
            letra_cifrada = abecedario[posicion_cifrada]

            decode_word += letra_cifrada
    return decode_word

def code_vigenere(palabra, clave):
    abecedario = string.ascii_lowercase
    palabra_codificada = []

    indice_clave = 0 

    for caracter in palabra:
        if caracter in abecedario:
            
            posicion_palabra = abecedario.index(caracter)
            
 
            posicion_clave = abecedario.index(clave[indice_clave % len(clave)])
            

            posicion_codificada = (posicion_palabra + posicion_clave) % 26
            
            
            letra_codificada = abecedario[posicion_codificada]
            palabra_codificada.append(letra_codificada)
            

            indice_clave += 1
        else:
            
            palabra_codificada.append(caracter)
            
    return "".join(palabra_codificada)

def decode_vigenere(palabra_codificada, clave):

    abecedario = string.ascii_lowercase
    palabra_descodificada = []
    
    indice_clave = 0

    for caracter_codificado in palabra_codificada:
        if caracter_codificado in abecedario:

            posicion_codificada = abecedario.index(caracter_codificado)
            

            posicion_clave = abecedario.index(clave[indice_clave % len(clave)])
            

            posicion_descodificada = (posicion_codificada - posicion_clave) % 26
            

            letra_descodificada = abecedario[posicion_descodificada]
            palabra_descodificada.append(letra_descodificada)
            
            indice_clave += 1
        else:

            palabra_descodificada.append(caracter_codificado)
            
    return "".join(palabra_descodificada)



def main():
    

    while True:
        selecFormat = int(input("Que metodo quiere utilizar: \n 1.- Cesar \n 2.- Vigenere \n"))
        if selecFormat == 1:
            frase_simpl = simpli_frase()
            while True:
                selecEmcript = int(input("Que desea encriptar o desencriptar: 1/2 \n"))
                if selecEmcript == 1:
                    print(code_cesar(frase_simpl))
                    break
                elif selecEmcript == 2:
                    print(decode_cesar(frase_simpl))
                    break
            break
            
        elif selecFormat == 2:
            frase_simpl = simpli_frase()
            while True:
                key_word = input("Indique que palabra quiere sera la 'clave' \n")
                selecEmcript = int(input("Que desea encriptar o desencriptar: 1/2 \n"))
                if selecEmcript == 1:
                    print(code_vigenere(frase_simpl,key_word))
                    break
                elif selecEmcript == 2:
                    print(decode_vigenere(frase_simpl,key_word))
                    break
            break
    
    


if __name__ == "__main__":
    main()