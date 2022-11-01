def ingresoLetra(letrasBuenas, letrasMalas):
    letra = input("Ingrese una letra (0 o esc salir): ")
    while letra in letrasBuenas or letra in letrasMalas:
        print("letra repetida")
        letra = input("Ingrese una letra (0 o esc salir): ")
    return letra

def funcionEscape(letra):
    """ Evalua si escapas """
    intentoEscape = False
    if letra == "esc" or letra == "0":
        # print("Has salido")
        intentoEscape = True
    return intentoEscape
    
def correccionLetraMala(letra, letrasBuenas, letrasMalas):
    i = 0
    evaluacionLetra = None
    salida = []
    while i < 10:
        
        print("Ingreso erroneo")
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscapar = funcionEscape(letra)
        if intentoEscapar:
            evaluacionLetra = False
            i = 10
        else:
            letraValida = esSoloUnaLetra(letra)
            if letraValida:
                evaluacionLetra = True
                i = 10
            else:
                pass

    salida.append(letra)
    salida.append(evaluacionLetra)  
                 
    return salida            

def esSoloUnaLetra(letra):
    if len(letra) == 1 and letra.isalpha() is True:
        esLetra = True
    else: 
        esLetra = False
    
    return esLetra

def letraValida(letrasBuenas, letrasMalas):
    salidaLetra = []
    continuaJugando = None
    i = 0
    while i < 1:
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscape = funcionEscape(letra) 
        if intentoEscape:
            continuaJugando = False
            i = 10
        else:
            caracterValido = esSoloUnaLetra(letra)
            if caracterValido:
                continuaJugando = True
                i = 10
            else:
                devolucionDeCorrecion = correccionLetraMala(letra,letrasBuenas, letrasMalas)
                # print(f"acá hay que almacenar está variable en letras {devolucionDeCorrecion[0]}")
                if devolucionDeCorrecion[1]:
                    continuaJugando = True
                    letra = devolucionDeCorrecion[0]          
                    i = 10
                else:
                    continuaJugando = False
                    letra = devolucionDeCorrecion[0]
                    i = 10

    salidaLetra.append(letra)
    salidaLetra.append(continuaJugando)
    # print("salida buena está saliendo {}".format(salidaLetra))
    return salidaLetra

def letraBuena(letra, palabraElegida):
    esBuena = False
    if letra in palabraElegida:
        esBuena = True
    return esBuena

def muestraAciertosErrores(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado):
    
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    
    return None

def acumularLetras(letra, letras):
    letras += letra
    return letras

def muestraPalabraEncriptada(letras, palabraAhorcado):

    muestraParcial = ""
    for i in range (len(palabraAhorcado)):
        if palabraAhorcado[i] in letras:
            muestraParcial += palabraAhorcado[i]
        else:
            muestraParcial += "?"
    
    return muestraParcial

def printeoAciertoError(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado, letrasMalas):
    
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores}- {letrasMalas}  ")
    
    return None

def ganaPierdo(muestraParcial, palabraAhorcado, contadorErrores):

    if muestraParcial == palabraAhorcado:
        contadorErrores = 9
        print("HAS GANADO!")
    elif contadorErrores == 8:
        print("PERDISTE")
    else:
        pass

    return contadorErrores

def main():
    palabraElegida = "locura"
    letrasBuenas = ""
    letrasMalas = ""
    aciertos = 0 
    errores = 0 

    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {aciertos}  Desaciertos: {errores}")
    contador = 0
    while contador <= 7:

        salidaLetra = letraValida(letrasBuenas, letrasBuenas)
        sigueJugando = salidaLetra[1]
        letra = salidaLetra[0] 

        if sigueJugando: #tiene que evaluar si es letra buena o si es letra mala
                      
            esBuena = letraBuena(letra, palabraElegida)
            if esBuena:
                aciertos += 1
                letrasBuenas = acumularLetras(letra, letrasBuenas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores)
                    
            else:
                if letra not in letrasMalas:              
                    errores += 1
                    contador += 1
                    letrasMalas = acumularLetras(letra, letrasMalas)
                    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                    printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                    contador = ganaPierdo(muestraParcial, palabraElegida, errores)
                else:
                    print("Letra repetida")
        else:
            print("Has salido")
            contador = 10

    return None

main()