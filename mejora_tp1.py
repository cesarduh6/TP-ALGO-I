"""from texto import obtener_texto as texto_usar"""
texto_usar = """
    LAs az$ucena@s de blanco0_: raso e|rguíanse con cierto desmayo, com/o las
seño;.ritas en, en en en# t1ra2je@ de traje que que que que que la pobre había la..s camelias de color ca/rnoso hacían ,pensar.- en
tibias,,, desnudeces..., en grandes() señora|s indolentemente tendidas, mo0strando0 había Había
l[os misterio]s d°e s¨u piel de seda --_Borda, _Borda_ Bordeta_... nos asamos. ¡Por Dios! ¡Un traje de agua!
El valor del dólar blue tiene una diferencia sustancial con el dólar oficial, que se adquiere en los bancos y que posee una cotización establecida. Su venta es en el mercado informal, sin regulaciones ni límites, y por eso se opera generalmente a un valor mayor que el dólar oficial.
"""
longitud_minima = 5

def obtener_texto(texto_usar):
    texto_usar =  texto_usar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("ü","u").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N").replace("Ü","U").casefold()
    lista_texto = texto_usar.split()
    return lista_texto

texto = obtener_texto(texto_usar)


def eliminar_caracteres(lista_texto):
    """ 
    Función:
        eliminar_caracteres
    Parámetros: 
        lista_texto: transforma todo el texto que se le pase a lista
    Salidas:
        lista_solo_alfabetica: almacenará cada palabra del texto sin caracteres especiales, solo letras
    Precondiciones:
        Las palabras deben estar contenida solo por caracteres alfabéticos
    """
    lista_solo_alfabetica=[]
    for palabra in lista_texto:
        for caracter in palabra:
            if not caracter.isalpha():
                palabra = palabra.replace(caracter,"")
        lista_solo_alfabetica.append(palabra)
    return lista_solo_alfabetica

lista_filtrada_solo_alfabeticos = eliminar_caracteres(texto)

def filtrador_palabra(lista):
    """
    Función:
        filtrador_palabra
    Parámetros:
        lista: Lista que almacena palabras solo con caracteres alfabéticos
    Salidas:
        lista_aux: Lista que almacenará caracteres de todo el texto 
    Precondiciones:
        Que la palabras no contengan caracteres especiales, de longitud mayor a 5 caracteres , que no se repitan y sean alfabeticos
    """
    lista_aux = []
    for palabra in lista:
        palabra=palabra.lower()
        if len(palabra) >= longitud_minima and not palabra in lista_aux:
            lista_aux.append(palabra)
    return lista_aux
"""print(filtrador_palabra(lista_filtrada_solo_alfabeticos))"""

lista_filtrada_mayores_5 = filtrador_palabra(lista_filtrada_solo_alfabeticos)

def diccionarValido():
    texto = obtener_texto(texto_usar)
    lista_filtrada = eliminar_caracteres(texto)
    lista_caracteres_mayor_5 = filtrador_palabra(lista_filtrada)

    return lista_caracteres_mayor_5

def eligePorCantidad(longitud_Caracteres, lista_diccionario):
    """
    Función:
        lista_candidatas
    Parámetros:
        diccionario: Usamos la clave del diccionario que creamos con la cant. veces que se repite la palabra
        longitud: Usamos de referencia para filtrar la lista con palabras que tengan esa longitud
    Salidas:
        lista_candidatas: Almacena las posibles palabras que vayan a entrar al juego
    Precondiciones:
    """
    lista_candidatas = []
    if int(longitud_Caracteres) >= longitud_minima:
        for i in range (len(lista_diccionario)):
            if len(lista_diccionario[i]) == longitud_Caracteres:
                lista_candidatas.append(lista_diccionario[i])
    else:
        for i in range(len(lista_diccionario)):
            lista_candidatas.append(lista_diccionario[i])
    return lista_candidatas

def randomPalabraElegida(lista_candidatas):
    """
    Función:
        palabra_aleatoria
    Parámetros:
        lista_candidatas: Almacena las posibles palabras que vayan a entrar al juego
    Salidas:
        palabraSeleccionada: Elige una palabra al azar haciendo uso de la librería random
    Precondiciones:
    """
    from random import randint
    numeroMagico = int(randint(0,len(lista_candidatas)-1))
    palabraElegida = lista_candidatas[numeroMagico]
    return palabraElegida

def diccionario_palabras_repetidas(texto):
    """
    Función:
        diccionario_palabras_repetidas
    Parámetros:
        texto: usamos todo el texto sin caracteres especiales, para comprobar cuantas veces se repite la clave en ese texto
    Salidas:
        diccionario_palabra: diccionario que almacena como clave la palabra sin repetir y como valor las veces que se repite en todo el texto
    Precondiciones:
    """
    diccionario_palabra = {}
    contador_palabra = 0
    for palabra_filtrador in lista_filtrada_mayores_5:
        contador_palabra = texto.count(palabra_filtrador)
        diccionario_palabra[palabra_filtrador]=contador_palabra
    return dict(sorted(diccionario_palabra.items(), key = lambda diccionario:diccionario[0]))

"""print(diccionario_palabras_repetidas(lista_filtrada_solo_alfabeticos))"""


def validez_longitud():
    """
    Función:
        validez_longitud
    Parámetros:
        longitud: longitud mínima de los caracteres que almacenamos en la lista de filtrador_palabra
    Salidas:
        longitud: longitud que usaremos para filtrar el diccionario con las posibles palabras
    Precondiciones:
    """
    longitud = input("Ingrese longitud de la palabra que desea adivinar: ")
    while longitud == str(0) or not longitud.isnumeric():
        longitud = input("Error. Ingrese longitud de la palabra que desea adivinar: ")
    return longitud

def ingresoLetra(letrasBuenas, letrasMalas):
    """
    Función:
        ingresoLetra
    Parámetros:
        letrasBuenas: Acumulador de letras que coinciden con la palabra a adivinar
        letraMalas: Acumulador de letras que no coinciden con la palabra a adivinar
    Salidas:
        letra: Se retorna una letra que no pertenece 
    Precondiciones:
        Hay que ingresar una letra
    """
    letra = input("Ingrese una letra (0 o esc salir): ")
    while letra in letrasBuenas or letra in letrasMalas:
        print("letra repetida")
        letra = input("Ingrese una letra (0 o esc salir): ")
    return letra

def funcionEscape(letra):
    """
    Función:
        funcionEscape
    Parámetros:
        letra: letra que ingresó el usuario
    Salidas:
        intentoEscape: True si letra es "esc" o "0", False si letra no es "esc" o "0"
    """
    """ Evalua si escapas """
    return letra == "esc" or letra == "0"
    
def correccionLetraMala(letra, letrasBuenas, letrasMalas):
    """
    Función:
        correccionLetraMala
    Parámetros:
        * letra: Letra que ingresó el usuario
        * letrasBuenas: Almacena caracteres que están en la palabra a adivinar
        * letrasMalas: Almacena caracteres que NO están en la palabra a adivinar
    Salidas:
        * salida: Lista que contiene letra ingresada por el usuario y un Booleano
    Precondiciones:
        * Letra debe tener longitud mayor a 1
    Postcondiciones:
        * Devuelve un lista con la letra válida y un booleano para evaluar si continúas o no jugando
    """
    cant_control = 10
    variable_de_control = 0
    evaluacionLetra = None
    salida = []
    while variable_de_control < cant_control:
        print("Ingreso erroneo")
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscapar = funcionEscape(letra)
        if intentoEscapar:
            evaluacionLetra = False
            variable_de_control = cant_control
        else:
            letraValida = esSoloUnaLetra(letra)
            if letraValida:
                evaluacionLetra = True
                variable_de_control = cant_control
            else:
                pass
    salida.append(letra)
    salida.append(evaluacionLetra)          
    return salida       

def esSoloUnaLetra(letra):
    """
    Función:
        esSoloUnaLetra
    Parámetros:
        letra: Letra que ingresó el usuario
    Salidas:
        esLetra: Booleano - > Variable de control
    Precondiciones:
        La letra debe tener longitud 1 y ser alfabético
    """
    longitud_requerida = 1
    return len(letra) == longitud_requerida and letra.isalpha()

def letraValida(letrasBuenas, letrasMalas):
    """
    Función:
        letraValida
    Parámetros:
        * letrasBuenas: Almacena caracteres que están en la palabra a adivinar
        * letrasMalas: Almacena caracteres que NO están en la palabra a adivinar
    Salidas:
        * salidaLetra: Retorna una lista con una variable booleano y la letra ingresada
    Precondiciones:
        * Letra de longitud 1
        * Alfabetica
        * No se repita la letra
        * Evalua si continúas jugando o no
    """
    salidaLetra = []
    continuaJugando = None
    variable_de_control = 0
    while variable_de_control < 1:
        letra = ingresoLetra(letrasBuenas, letrasMalas)
        intentoEscape = funcionEscape(letra) 
        if intentoEscape:
            continuaJugando = False
            variable_de_control = 10
        else:
            caracterValido = esSoloUnaLetra(letra)
            if caracterValido:
                continuaJugando = True
                variable_de_control = 10
            else:
                devolucionDeCorrecion = correccionLetraMala(letra,letrasBuenas, letrasMalas)
                # print(f"acá hay que almacenar está variable en letras {devolucionDeCorrecion[0]}")
                if devolucionDeCorrecion[1]:
                    continuaJugando = True
                    letra = devolucionDeCorrecion[0]          
                    variable_de_control = 10
                else:
                    continuaJugando = False
                    letra = devolucionDeCorrecion[0]
                    variable_de_control = 10
    salidaLetra.append(letra)
    salidaLetra.append(continuaJugando)
    # print("salida buena está saliendo {}".format(salidaLetra))
    return salidaLetra

def letraBuena(letra, palabraElegida):
    """
    Función:
        letraBuena
    Parámetros:
        letra: Letra que ingresó el usuario
        palabraElegida: Palabra aleatoria que eligió el sistema
    Salidas:
        esBuena: Booleano -> Variable de Control
    Precondiciones:
        Que letra ingresada esté en la palabra elegida
    """
    return letra in palabraElegida

def muestraAciertosErrores(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado):
    """
    Función:
        muestraAciertosErrores
    Parámetros:
        letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado
    Salidas:
        Imprime el tablero
    """
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    
    return None

def acumularLetras(letra, letras):
    """
    Función:
        acumularLetras
    Parámetros:
        letra: Letra que ingresó el usuario
        letras: Variable que almacena TODOS LOS CARACTERES, estén o no estén en la palabra a adivinar
    Salidas:
        Letras acumuladas
    """
    letras += letra
    return letras

def muestraPalabraEncriptada(letras, palabraAhorcado):
    """
    Función:
        muestraPalabraEncriptada
    Parámetros:
        letras: Variable que almacenó TODOS LOS CARACTERES, estén o no estén en la palabra a adivinar
        palabraAhorcado: palabra aleatoria elegida por el sistema
    Salidas:
        Encripta la palabra 
    """
    muestraParcial = ""
    for i in range (len(palabraAhorcado)):
        if palabraAhorcado[i] in letras:
            muestraParcial += palabraAhorcado[i]
        else:
            muestraParcial += "?"
    
    return muestraParcial

def printeoAciertoError(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado, letrasMalas):
    """
    Función: 
        printeoAciertoError
    Parámetros:
        letra: 
        muestraParcial: palabra a adivinar en formato "?"
        contadorAciertos: cantidad de aciertos de la partida
        contadorErrores: cantidad de desaciertos de la partida
        palabraAhorcado: palabra aleatoria elegida por el sistema
        letrasMalas: variable que almacena todos los caracteres erróneos
    Salidas:
        Imprime el tablero

    """
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} - {letrasMalas}")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} - {letrasMalas} ")
    
    return None

def ganaPierdo(muestraParcial, palabraAhorcado, contadorErrores,puntaje):
    """
    Función: 
        ganaPierdo
    Parámetros:
        muestraParcial: transforma palabra a adivinar en "?"
        palabraAhorcado: palabra aleatoria elegida por el sistema
        contadorErrores
        puntaje: puntaje total por partida
    Salidas:
        Imprime si ganó o perdió el usuario
    """
    if muestraParcial == palabraAhorcado:
        contadorErrores = 9
        print(f"\nHAS GANADO! SU PUNTAJE ES: {puntaje}\n")
        # nueva_partida(puntaje)
    elif contadorErrores == 8:
        print(f"\nPERDISTE! SU PUNTAJE ES: {puntaje}\nPalabra a adivinar era: {palabraAhorcado}\n")
        # nueva_partida(puntaje)
    else:
        pass
    return contadorErrores

def Asignacion_Puntajes(tot_ganados,tot_perdidos):
    """
    Función: 
        Asignacion_Puntajes
    Parámetros:
        tot_ganados: Acumula la cantidad de puntos por cada acierto
        tot_perdidos: Acumula la cantidad de puntos por cada desacierto
    Salidas:
        Retorna el puntaje total
    """
    return tot_ganados + tot_perdidos

def nueva_partida():
    """
    Función: nueva_partida
    Parámetros:
        puntaje_anterior: Almacena el puntaje acumulador de todas las partidas jugadas
    Salidas:
        tot: Acumula el puntaje de todas las partidas jugadas
    """
    consulta_nueva_partida = ""

    total = jugar()

    variable_de_control = 1
    while variable_de_control != 0:
        consulta_nueva_partida = input("Desea jugar una nueva partida? (s/n): ")

        if consulta_nueva_partida == "s": 
            puntaje_nuevo = jugar()
            total += puntaje_nuevo
            print(f"\nEL TOTAL DE LAS PARTIDAS JUGADAS {total}\n")
        else:    
            print(f"\nEL TOTAL DE LAS PARTIDAS JUGADAS {total}")
            variable_de_control = 0
    
    return None


def jugar():
    errores = 0
    aciertos = 0 
    contador = 0
    letrasMalas = ""
    letrasBuenas = ""
    cant_intentos = 7
    puntos_por_acierto = 10
    puntos_por_desaciertos = -5
    total_puntajes_ganados = 0
    total_puntajes_perdidos = 0
    longitud = int(validez_longitud())
    lista_diccionario = diccionarValido()
    lista_Igualdad_Caracteres = eligePorCantidad(longitud, lista_diccionario)
    palabraElegida = randomPalabraElegida(lista_Igualdad_Caracteres)
    puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {aciertos}  Desaciertos: {errores}")
    while contador <= cant_intentos:

        salidaLetra = letraValida(letrasBuenas, letrasBuenas)
        sigueJugando = salidaLetra[1]
        letra = salidaLetra[0] 

        if sigueJugando:

            esBuena = letraBuena(letra, palabraElegida)

            if esBuena:
                aciertos += 1
                total_puntajes_ganados = aciertos * puntos_por_acierto
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                letrasBuenas = acumularLetras(letra, letrasBuenas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores,puntaje)
                    
            elif letra not in letrasMalas: 
                errores += 1
                total_puntajes_perdidos = errores * puntos_por_desaciertos
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                contador += 1
                letrasMalas = acumularLetras(letra, letrasMalas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores,puntaje)
            else:
                print("LETRA REPETIDA")
        else:
            contador = 10
            print("\nJUEGO FINALIZADO\n")


    return puntaje


nueva_partida()