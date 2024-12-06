

import random


def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'angular', 'django', 'tensorflow', 'react', 'git', 'flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("¡Bienvenido al juego del ahorcado")
    print(f"Tenés {intentos} intentos para adivinar la siguiente palabra secreta: ")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas), " (Tiene ", len(palabra_secreta), " letras en total)")

    while not juego_terminado:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Por favor introduzca una letra valida (sólo caracteres alfabeticos)")
        elif adivinanza in letras_adivinadas:
            print("Ya has utilizado esa letra, proba con una nueva")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print("¡Muy bien has acertado una letra de la palabra secreta!")
                print(f"La letra {adivinanza} es correcta.")
            else:
                intentos -= 1
                print(f"Lo siento mucho, la letra {adivinanza} no está presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos")
        
        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"¡Felicitaciones has ganado! La palabra secreta es: {palabra_secreta}")

    if intentos == 0:
        print(f"Lo sentimos mucho se te acabaron los intentos, la palabra secreta era {palabra_secreta}")

juego_ahorcado()