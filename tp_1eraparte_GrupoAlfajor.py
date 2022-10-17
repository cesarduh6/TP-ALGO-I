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

palabraElegida= elegirPalabra(diccionarioPalabras())

def mostrar_simbolo(palabra):
    caracter = "?"
    muestraParcial = len(palabraAhorcado)*caracter
    return muestraParcial
    
"""print(mostrar_simbolo(palabraElegida))"""

def jugabilidad(palabra):

    contadorAciertos = 0
    contadorErrores = 0
    caracteresErroneos = ''
    letraSinInterrogacion = ''

    print(f"Palabra a adivinar: {palabra}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores}")
    letra = input("Ingrese una letra: ")
    

    while contadorErrores <= 7:
        for posicion in range (0,len(palabra)):
            if letra in palabra:
                contadorAciertos += 1
                letraSinInterrogacion = 'r?????'
                print(f"Muy bien!!! -> {letraSinInterrogacion}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores}")
                letra = input("Ingrese una letra: ")
            else:
                contadorErrores +=1       
                caracteresErroneos += letra 
                print(f"Lo siento!!! -> {letraSinInterrogacion}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores} - {caracteresErroneos}")
                letra = input("Ingrese una letra: ")

        if contadorErrores == 8:
            print("Perdiste")

    return None

def main():

    
    jugabilidad(palabraElegida)

main()