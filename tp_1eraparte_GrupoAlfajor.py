from random import randint
caracteresErroneos = ''
Aciertos = 0
Desaciertos = 0
longitud_minima = 5
texto_usar = """
    LAs az$ucena@s de blanco0_: raso e|rguíanse con cierto desmayo, com/o las
seño;.ritas en, en en en# t1ra2je@ de traje que que que que que la pobre había la..s camelias de color ca/rnoso hacían ,pensar.- en
tibias,,, desnudeces..., en grandes() señora|s indolentemente tendidas, mo0strando0 había Había
l[os misterio]s d°e s¨u piel de seda --_Borda, _Borda_ Bordeta_... nos asamos. ¡Por Dios! ¡Un traje de agua!
"""

#Primero tenemos que generar la palabra aleatoria para poderla usar en el tablero

# ---------------- GENERAR LISTA/DICCIONARIO TP PARTE 2 --------------------- #

def F_lista_texto(texto_usar):
    """caracteres_especiales_A = 'áÁàÀäÄ'
    caracteres_especiales_E = 'éÉèÈëË'
    caracteres_especiales_I = 'íÍìÌïÏ'
    caracteres_especiales_O = 'óÓòÒöÖ'
    caracteres_especiales_U = 'úÚùÙüÜ'
    for caracter in texto_usar:
        if caracter in caracteres_especiales_A:
            texto_usar[caracter].replace(caracter,"a")
        elif caracter in caracteres_especiales_E:
            texto_usar[caracter].replace(caracter,"e")
        elif caracter in caracteres_especiales_I:
            texto_usar[caracter].replace(caracter,"i")
        elif caracter in caracteres_especiales_O:
            texto_usar[caracter].replace(caracter,"o")
        elif caracter in caracteres_especiales_U:
            texto_usar[caracter].replace(caracter,"u")"""
    texto_usar =  texto_usar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("ü","u").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N").replace("Ü","U").casefold()
    lista_texto = texto_usar.split()
    return lista_texto

lista_texto = F_lista_texto(texto_usar)

def eliminar_caracteres(lista_texto):
    #lista_solo_alfabetica -> almacenará cada palabra del texto sin caracteres especiales, solo letras
    lista_solo_alfabetica=[]
    for palabra in lista_texto:
        for caracter in palabra:
            if not caracter.isalpha():
                palabra = palabra.replace(caracter,"")
        lista_solo_alfabetica.append(palabra)
    return lista_solo_alfabetica

lista_filtrada_solo_alfabeticos = eliminar_caracteres(lista_texto)

def F_filtrar_lista_texto(texto):
    #Lista_aux -> Lista que almacenará caracteres de todo el texto (sin caracteres especiales) con >= 5 caracteres, que no se repitan y sean alfabeticos
    lista_aux = []
    for palabra in texto:
        palabra=palabra.lower()
        if len(palabra) >= longitud_minima and not palabra in lista_aux:
            lista_aux.append(palabra)
    return lista_aux

lista_filtrada_mayores_5 = F_filtrar_lista_texto(lista_filtrada_solo_alfabeticos)

def diccionario(texto):
    #diccionario_palabra -> almacenará como 'clave' cada palabra sin repetirse y como 'valor' la cantidad de veces que se repite la clave en todo el texto sin caracteres especiales
    #contador_palabra -> contará la cantidad de veces que se repite la palabra en el texto sin caracteres especiales
    diccionario_palabra = {}
    contador_palabra = 0
    for palabra_filtrador in F_filtrar_lista_texto(lista_filtrada_solo_alfabeticos):
        contador_palabra = texto.count(palabra_filtrador)
        diccionario_palabra[palabra_filtrador]=contador_palabra
    return dict(sorted(diccionario_palabra.items(), key = lambda diccionario:diccionario[0]))

# --------------- ELEGIR PALABRA ALEATORIA TP PARTE 3 ----------------- #

diccionario_usar = diccionario(lista_filtrada_solo_alfabeticos)

def validez_longitud(longitud):
    longitud = int(input("Ingrese longitud de la palabra que desea adivinar: "))
    while longitud < 1:
        longitud = int(input("Error. Ingrese longitud de la palabra que desea adivinar: "))
    return longitud

pedir_longitud_palabra= validez_longitud(longitud_minima)

def lista_candidatas(diccionario,longitud):
    lista_candidatas = []
    if longitud >= longitud_minima :
        #Asumiendo que el jugador ingresa alguna longitud  
        """print(f"Solo juegan las palabras con {longitud} caracteres")"""
        for clave in diccionario:
            if len(clave) == longitud:
                lista_candidatas.append(clave)
    else:
        #Si no ingresa una longitud o ingresa "cero", juegan todas las palabras
        """print("Juegan todas las palabras")"""
        for clave in diccionario:
            lista_candidatas.append(clave)
    return lista_candidatas


palabras_candidatas = lista_candidatas(diccionario_usar,pedir_longitud_palabra)

def palabra_aleatoria(lista_candidatas):
    palabraSeleccionada = lista_candidatas[randint(1,len(lista_candidatas)-1)]
    return palabraSeleccionada

palabra_a_adivinar = palabra_aleatoria(palabras_candidatas)


# ------------------ ESTRUCTURA TP PARTE 1 ---------------------- #


def F_Palabra_Con_Caracter_Especial(palabra_aleatoria):
    palabra_aleatoria = palabra_aleatoria.lower()
    caracter = "?"
    return len(palabra_aleatoria)*caracter

palabra_hecha_simbolo = F_Palabra_Con_Caracter_Especial(palabra_a_adivinar)

def F_tablero(Palabra_a_Adivinar, Num_Aciertos, Num_Desaciertos):
    return print(f"Palabra a adivinar: {Palabra_a_Adivinar}    Acierto: {Num_Aciertos}     Desaciertos: {Num_Desaciertos}")

tablero = F_tablero(palabra_hecha_simbolo,Aciertos, Desaciertos)

def F_ingresar_0_o_FIN(letra):
    pass

def F_ingreso_letra():
    caracteres_acentuados = 'áÁàÀéÉèÈíÍìÌóÓòÒúÚùÙ'
    dieresis = 'äÄëËïÏöÖüÜ'
    tablero
    letra = input("Ingrese una letra: ")
    F_ingresar_0_o_FIN(letra)
    while  letra.isupper() or len(letra)>1 or letra.isnumeric() or not letra.isalnum() or letra in caracteres_acentuados or letra in dieresis:
        tablero
        letra = input("Error. Ingrese nuevamente una letra: ")
    return letra

ingreso_letra = F_ingreso_letra()


"""def F_DesbloquearCaracteres(letra_ingresada, palabra_aleatoria,cant_Aciertos,cant_Desaciertos,car_Erroneo):
    muestraParcial = ""
    for caracter in range (len(palabra_aleatoria)):
        if palabra_aleatoria[caracter] in letra_ingresada:
            muestraParcial += palabra_aleatoria[caracter]
            cant_Aciertos+=1
        else:
            muestraParcial += "?"
            cant_Desaciertos+=1
            car_Erroneo += letra_ingresada
    return muestraParcial"""



# ----------- VARIABLES PARA LLAMAR CADA FUNCION ---------------------#


def main(cant_Aciertos, cant_Desaciertos, car_Erroneo):
    #--------GENERAR EL DICCIONARIO PARA SABER QUE PALABRA HAY QUE ADIVINAR ------------#
    muestraParcial = ""
    pedir_longitud_palabra
    palabra_a_adivinar
    while cant_Desaciertos <=7:
        ingreso_letra
        # ----- El problema aquí es que no me desbloquea el caracter ingresado correctamente ----- #
        for caracter in range(len(palabra_a_adivinar)):
            if palabra_a_adivinar[caracter] in ingreso_letra:
                muestraParcial += palabra_a_adivinar[caracter]
                cant_Aciertos+=1
            else:
                muestraParcial += "?"
                cant_Desaciertos+=1
                car_Erroneo += ingreso_letra
        print(cant_Aciertos)
        print(cant_Desaciertos)
        print(car_Erroneo)
        
    return None
main(Aciertos, Desaciertos,caracteresErroneos)