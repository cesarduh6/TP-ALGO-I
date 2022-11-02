from random import randint
#----------------------------------------- PARTE 2 --------------------------------------------#
texto_usar = """
    LAs az$ucena@s de blanco0_: raso e|rguíanse con cierto desmayo, com/o las
seño;.ritas en, en en en# t1ra2je@ de traje que que que que que la pobre había la..s camelias de color ca/rnoso hacían ,pensar.- en
tibias,,, desnudeces..., en grandes() señora|s indolentemente tendidas, mo0strando0 había Había
l[os misterio]s d°e s¨u piel de seda --_Borda, _Borda_ Bordeta_... nos asamos. ¡Por Dios! ¡Un traje de agua!
"""

"""from texto import obtener_texto as texto_usar"""
texto_usar =  texto_usar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("ü","u").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N").replace("Ü","U").casefold()
lista_texto = texto_usar.split()
longitud_minima = 5

def eliminar_caracteres(lista_texto):
    #lista_solo_alfabetica -> almacenará cada palabra del texto sin caracteres especiales, solo letras
    lista_solo_alfabetica=[]
    for palabra in lista_texto:
        for caracter in palabra:
            if not caracter.isalpha():
                palabra = palabra.replace(caracter,"")
        lista_solo_alfabetica.append(palabra)
    return lista_solo_alfabetica
"""print(eliminar_caracteres(lista_texto))"""

lista_filtrada_solo_alfabeticos = eliminar_caracteres(lista_texto)

def filtrador(texto):
    #Lista_aux -> Lista que almacenará caracteres de todo el texto (sin caracteres especiales) con >= 5 caracteres, que no se repitan y sean alfabeticos
    lista_aux = []
    for palabra in texto:
        palabra=palabra.lower()
        if len(palabra) >= longitud_minima and not palabra in lista_aux:
            lista_aux.append(palabra)
    return lista_aux
"""print(filtrador(lista_filtrada_solo_alfabeticos))"""

lista_filtrada_mayores_5 = filtrador(lista_filtrada_solo_alfabeticos)

def diccionario(texto):
    #diccionario_palabra -> almacenará como 'clave' cada palabra sin repetirse y como 'valor' la cantidad de veces que se repite la clave en todo el texto sin caracteres especiales
    #contador_palabra -> contará la cantidad de veces que se repite la palabra en el texto sin caracteres especiales
    diccionario_palabra = {}
    contador_palabra = 0
    for palabra_filtrador in filtrador(lista_filtrada_solo_alfabeticos):
        contador_palabra = texto.count(palabra_filtrador)
        diccionario_palabra[palabra_filtrador]=contador_palabra
    return dict(sorted(diccionario_palabra.items(), key = lambda diccionario:diccionario[0]))

"""print(diccionario(lista_filtrada_solo_alfabeticos))"""

# ------------------------------------------------- ETAPA 3 -------------------------------------- #

diccionario_usar = diccionario(lista_filtrada_solo_alfabeticos)
"""print(diccionario_usar)"""

def validez_longitud(longitud):
    longitud = int(input("Ingrese longitud de la palabra que desea adivinar: "))
    while longitud == 0:
        longitud = int(input("Error. Ingrese longitud de la palabra que desea adivinar: "))
    return longitud

longitud_palabra= validez_longitud(longitud_minima)

def lista_candidatas(diccionario,longitud):
    lista_candidatas = []
    if longitud >= 5 :
        #Asumiendo que el jugador ingresa alguna longitud  
        print(f"Solo juegan las palabras con {longitud} caracteres")
        for clave in diccionario:
            if len(clave) == longitud:
                lista_candidatas.append(clave)
    else:
        #Si no ingresa una longitud o ingresa "cero", juegan todas las palabras
        print("Juegan todas las palabras")
        for clave in diccionario:
            lista_candidatas.append(clave)
    return lista_candidatas

"""print(lista_candidatas(diccionario_usar,longitud_palabra))"""

palabras_candidatas = lista_candidatas(diccionario_usar,longitud_palabra)

def palabra_aleatoria(lista_candidatas):
    palabraSeleccionada = lista_candidatas[randint(1,len(lista_candidatas)-1)]
    return palabraSeleccionada

palabra_a_adivinar = palabra_aleatoria(palabras_candidatas)
"""print(f"Palabra elegida: {palabra_aleatoria(palabras_candidatas)}")"""


# ------------------------------------------- ETAPA 1 ----------------------------------------- #

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

def printeoAciertoError(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado, letrasMalas, puntaje):
    
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} Puntaje: {puntaje}")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores}- {letrasMalas} - Puntaje: {puntaje} ")
    
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

def Asignacion_Puntajes(tot_ganados,tot_perdidos):
    return tot_ganados + tot_perdidos

def nueva_partida():
    consulta_nueva_partida = input("Desea jugar una nueva partida? (s/n): ")
    while consulta_nueva_partida != 'n':
        main()
        consulta_nueva_partida = input("Desea jugar una nueva partida? (s/n): ")
    return consulta_nueva_partida

def main():
    palabraElegida = palabra_a_adivinar
    letrasBuenas = ""
    letrasMalas = ""
    aciertos = 0 
    errores = 0 
    total_puntajes_ganados = 0
    total_puntajes_perdidos = 0
    puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
    muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {aciertos}  Desaciertos: {errores} Puntaje: {puntaje}")
    contador = 0
    while contador <= 7:

        salidaLetra = letraValida(letrasBuenas, letrasBuenas)
        sigueJugando = salidaLetra[1]
        letra = salidaLetra[0] 

        if sigueJugando: #tiene que evaluar si es letra buena o si es letra mala

            esBuena = letraBuena(letra, palabraElegida)

            if esBuena:
                aciertos += 1
                total_puntajes_ganados = aciertos * 10
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                letrasBuenas = acumularLetras(letra, letrasBuenas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas,puntaje)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores)
                    
            elif letra not in letrasMalas: 
                errores += 1
                total_puntajes_perdidos = errores * -5
                puntaje = Asignacion_Puntajes( total_puntajes_ganados, total_puntajes_perdidos)
                contador += 1
                letrasMalas = acumularLetras(letra, letrasMalas)
                muestraParcial = muestraPalabraEncriptada(letrasBuenas, palabraElegida)
                printeoAciertoError(letra, muestraParcial, aciertos, errores, palabraElegida, letrasMalas, puntaje)
                contador = ganaPierdo(muestraParcial, palabraElegida, errores)
            else:
                print("Letra repetida")
        else:
            print("Has salido")
            contador = 10
    nueva_partida()
    return None

main()