from random import randint


def autor():
    return "Manuel Jesus Sanchez Vega"


def damePalabra():
    listaPalabras = ["telefono", "cartera", "monitor", "reparacion"]
    # Devuelve una palabra aleatoria de la lista
    return listaPalabras[randint(0, len(listaPalabras) - 1)]


def recuadro(texto, h_char, v_char):
    print(h_char * (len(texto) + 2))
    print(v_char, texto, v_char, sep="")
    print(h_char * (len(texto) + 2))
    print("\n")


def formarPalabra(usadas, pal):
    temporal = ""
    #oculta la palabra con guiones bajos, excepto los caracteres que esten en 'usadas'
    for x in pal:
        if x in usadas:
            temporal = temporal + x
        else:
            temporal = temporal + "_"
    return temporal

def escena(pal, usadas, intentos, fallos):

    dibujar(fallos)
    #forma la palabra temporal, que va a ser la que contiene guiones bajos, la que el usuario va a ver
    palabraTemporal = formarPalabra(usadas, pal)
    print("--------|---------\t", palabraTemporal, sep="")

    print("<", sep="", end="")
    for x in usadas:
        print(x, sep="", end="")
    print("> Intentos={}".format(intentos), sep="", end="")

#Metodo que, segun el numero de fallos que se le pase, dibuja un munneco u otro
def dibujar(intentos):
    if intentos == 0:
        print("\t|", "\t|", "\t|", "\t|", sep="\n")
    elif intentos == 1:
        print("\t----------", "\t|", "\t|", "\t|", "\t|", sep="\n")
    elif intentos == 2:
        print("\t----------", "\t|\t |", "\t|", "\t|", "\t|", sep="\n")
    elif intentos == 3:
        print("\t----------", "\t|\t |", "\t|\t\\O/", "\t|", "\t|", sep="\n")
    elif intentos == 4:
        print("\t----------", "\t|\t |", "\t|\t\\O/", "\t|\t |", "\t|", sep="\n")
    else:
        print("\t----------", "\t|\t |", "\t|\t\\O/",
              "\t|\t |", "\t|\t/ \\", sep="\n")


def pideLetra(usadas):
    letra = "99"
    # comprueba si el tamanno es 1, si no esta la letra usada y si es una letra, no un numero ni simbolo
    while len(letra) != 1 or letra.upper() in usadas or letra[0].isalpha() is False:
        letra = input("\tIntroduce una letra: ")
    return letra


def comprueba(palabra, usadas, letra, fallos):
    fallosMax = 5
    continuar = True
    gana = False

    if letra.upper() not in palabra.upper():
        fallos += 1

    if fallos == fallosMax:
        gana = False
        continuar = False
    else:
        usadas.append(letra.upper())

        # Recorre las palabras usadas para ver si estan todas en la palabra escondida y ver si gana
        contador = 0
        for x in palabra:
            if x in usadas:
                contador += 1
        if contador == len(palabra):
            gana = True
            continuar = False

    return continuar, gana, usadas, fallos


# Obtener una palabra a adivinar
palabra = damePalabra().upper()

# Letras que ya se han usado, la primera se muestra y se annade a la lista de usadas
usadas = []
usadas.append(palabra[0])

# intentos realizados y fallos cometidos
fallos = 0
intentos = 0

# Mensaje de inicio
recuadro("Juego del Ahorcado - creado por " + autor(), "#", "#")
recuadro("Comienza el juego", "=", "|")

continuar = True
while continuar:
    escena(palabra, usadas, intentos, fallos)
    letra = pideLetra(usadas)
    intentos += 1
    continuar, gana, usadas, fallos = comprueba(palabra, usadas, letra, fallos)

if gana:
    recuadro("Has ganado en {} intentos, la palabra era {}".format(intentos, palabra), "*", "*")
else:
    #Si pierde, dibuja el munneco entero
    dibujar(5)
    recuadro("Has perdido. La palabra era {}".format(palabra), "-", "|")
