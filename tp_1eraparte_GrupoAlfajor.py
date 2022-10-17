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


    contadorAciertos = 0
    contadorErrores = 0

    
    letra = input("Ingrese una letra (0 o esc salir): ")

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores}")

    while contadorErrores <= 7 and not letra.isnumeric() and len(letra)==1:

    """    muestraParcial = ""
        letra = input("Ingrese una letra (0 o esc salir): ")

        if len(letra)> 1 or not letra.isalpha():
            print("Ingreso erroneo")
            letra = input("Ingrese una letra (0 o esc salir): ")

        letra += letra

        if letra not in palabraAhorcado:
            contadorErrores += 1
            # print(f"contador intentos {contadorErrores}")
        else:
            contadorAciertos += 1
        

        for i in range (len(palabraAhorcado)):
            if palabraAhorcado[i] in letra:
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
            print("PERDISTE")"""

    
    return None


def main():

    palabraElegida= elegirPalabra(diccionarioPalabras())
    jugabilidad(palabraElegida)

main()