from random import randint

def diccionarioPalabras():
    listado = ["casa", "auto", "casita", "alfajor", "amistad", "empeño", "gladiador", "jugador", "basquet",
    "roquero", "principe", "princesa", "caperucita", "onomatopeya", "clembuterol", "circulo"]
    # listado.sort()
    return listado


def elegirPalabra(listado):
    palabraSeleccionada = listado[randint(1,len(listado)-1)]
    # print(palabraSeleccionada)
    return palabraSeleccionada

def jugabilidad(palabra):

    palabraAhorcado = palabra.lower()
    caracter = "?"
    muestraParcial = len(palabraAhorcado)*caracter
    print(palabraAhorcado)


    contadorAciertos = 0
    contadorErrores = 0

    letras = ""

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores}")

    while contadorErrores <= 7:


        muestraParcial = ""
        letra = input("Ingrese una letra (0 o esc salir): ")

        if len(letra)> 1 or not letra.isalpha():
            print("Ingreso erroneo")
            letra = input("Ingrese una letra (0 o esc salir): ")
        elif letra == "0" or letra == "esc":
            print("has escapado! ")
            # contadorErrores = 10

        letras += letra

        if letra not in palabraAhorcado:
            contadorErrores += 1
            # print(f"contador intentos {contadorErrores}")
        else:
            contadorAciertos += 1
        

        for i in range (len(palabraAhorcado)):
            if palabraAhorcado[i] in letras:
                muestraParcial += palabraAhorcado[i]
            else:
                muestraParcial += caracter

        if letra in muestraParcial:
            print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
        else:
            print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")

        if muestraParcial == palabraAhorcado:
            print("HAS GANADO!")
            contadorErrores = 15
        
        if contadorErrores == 8:
            print("PERDISTE")

    
    return None


def main():

    palabraElegida= elegirPalabra(diccionarioPalabras())
    jugabilidad(palabraElegida)

main()