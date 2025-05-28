'''
Conceptos Generales para ambos algoritmos:

Entrada y Salida:

¿Cómo vas a obtener el texto que el usuario quiere cifrar/descifrar? Piensa en input().
¿Cómo vas a mostrar el resultado (texto cifrado/descifrado)? Piensa en print().
¿Cómo vas a permitir al usuario elegir entre cifrar o descifrar, y qué algoritmo usar? Un menú simple con if/elif/else podría ser útil.
Manejo de Mayúsculas/Minúsculas y Caracteres No Alfabéticos:

¿Qué pasa si el usuario introduce una frase con mayúsculas y minúsculas? ¿Quieres tratarlas igual? str.lower() o str.upper() te serán útiles.
¿Qué ocurre con los espacios, números o signos de puntuación? ¿Quieres ignorarlos, mantenerlos, o cifrarlos también? La forma más sencilla suele ser ignorarlos o mantenerlos sin cambios. Puedes usar str.isalpha() para verificar si un carácter es una letra.
Iteración sobre el texto:

Para procesar cada carácter del texto, necesitarás un bucle for.
Algoritmo de Cifrado César:

Este es el más sencillo y una excelente forma de empezar.

La Lógica del Cifrado César:

Se basa en desplazar cada letra del alfabeto un número fijo de posiciones. Por ejemplo, con un desplazamiento de 3, 'A' se convierte en 'D', 'B' en 'E', etc.
¿Qué pasa cuando llegas al final del alfabeto (por ejemplo, con un desplazamiento de 3, ¿qué pasa con 'X', 'Y', 'Z'?) Piensa en la modularidad o el "efecto de círculo". El operador % (módulo) en Python te será muy útil aquí.
Representación de Caracteres:

Las computadoras no entienden las letras directamente, sino sus valores numéricos. Python tiene funciones para convertir entre caracteres y sus valores ASCII/Unicode.
Investiga las funciones ord() (carácter a número) y chr() (número a carácter).
¿Cuál es el valor numérico de 'a' y 'z' (o 'A' y 'Z')? Esto es crucial para calcular los desplazamientos relativos.
Implementación del Cifrado:

Para cada letra en el texto original:
Obtén su valor numérico.
Calcula su posición relativa dentro del alfabeto (ej. 'a' es 0, 'b' es 1, etc.).
Aplica el desplazamiento y usa el operador módulo para "volver" al principio del alfabeto si te pasas.
Convierte el nuevo valor numérico de vuelta a un carácter.
Añade este nuevo carácter al texto cifrado.
Implementación del Descifrado:

El descifrado César es simplemente el cifrado César con un desplazamiento en la dirección opuesta. ¿Cómo puedes expresar eso matemáticamente?
Algoritmo de Cifrado Vigenère:

Este es un poco más complejo que César, ya que utiliza una "clave" de texto.

La Lógica del Cifrado Vigenère:

Combina el texto plano con una palabra clave. Cada letra del texto plano se cifra usando una letra diferente de la clave, que se repite.
Por ejemplo, si la clave es "KEY" y el texto es "HELLO":
'H' se cifra con 'K'.
'E' se cifra con 'E'.
'L' se cifra con 'Y'.
'L' se cifra con 'K' (la clave se repite).
'O' se cifra con 'E' (la clave se repite).
Relación con César:

Cada paso del cifrado Vigenère es esencialmente un cifrado César, donde el desplazamiento está determinado por la letra correspondiente de la clave.
Manejo de la Clave:

La clave debe repetirse para cubrir todo el texto plano. ¿Cómo puedes hacer esto de forma eficiente?
¿Qué pasa si la clave es más corta o más larga que el texto?
Necesitarás un índice para recorrer tanto el texto plano como la clave, y este índice para la clave deberá "reiniciarse" cuando llegue al final de la clave. El operador % también te será muy útil aquí.
Implementación del Cifrado:

Para cada letra en el texto original:
Determina la letra de la clave que le corresponde (usando el índice de la clave con el operador módulo).
Calcula el "desplazamiento" que esa letra de la clave representa (similar a cómo calculaste los desplazamientos para César).
Aplica este desplazamiento a la letra del texto plano, usando las mismas funciones ord() y chr() y el operador módulo que usaste en César.
Añade el carácter cifrado al resultado.
Avanza el índice de la clave.
Implementación del Descifrado:

El descifrado Vigenère es el inverso del cifrado. Si para cifrar sumabas el desplazamiento de la clave, para descifrar, ¿qué operación harías? Piensa en la resta y el operador módulo para manejar los valores negativos.
Estructura General del Código (sugerencia):

Una función cifrar_cesar(texto, clave_desplazamiento)
Una función descifrar_cesar(texto_cifrado, clave_desplazamiento)
Una función cifrar_vigenere(texto, clave)
Una función descifrar_vigenere(texto_cifrado, clave)
Una función main() que maneje la interacción con el usuario (menú, llamadas a las funciones de cifrado/descifrado).

'''
def main():
    frase = input("Introduzaca la frase que quiera encriptar o desencriptar \n").lower()

    while True:
        selecEmcript = int(input("Que desea encriptar o desencriptar: 1/2 \n"))
        if selecEmcript == 1 or selecEmcript == 2:
            break
    
    while True:
        selecFormat = int(input("Que metodo quiere utilizar: 1/2 \n"))
        if selecFormat == 1 or selecFormat == 2:
            break

    print(f"La frase {frase} la seleccion es {selecEmcript} y la seleccion es {selecFormat}")

if __name__ == "__main__":
    main()