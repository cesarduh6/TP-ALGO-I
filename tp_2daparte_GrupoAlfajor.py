from random import randint
texto_usar = """
    LAs az$ucena@s de blanco0_: raso e|rguíanse con cierto desmayo, com/o las
seño;.ritas en, en en en# t1ra2je@ de traje que que que que que la pobre había la..s camelias de color ca/rnoso hacían ,pensar.- en
tibias,,, desnudeces..., en grandes() señora|s indolentemente tendidas, mo0strando0 había Había
l[os misterio]s d°e s¨u piel de seda --_Borda, _Borda_ Bordeta_... nos asamos. ¡Por Dios! ¡Un traje de agua!
"""

"""from texto import obtener_texto as texto_usar"""
def obtener_texto(texto_usar):
    texto_usar =  texto_usar.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace("ü","u").replace("Á","A").replace("É","E").replace("Í","I").replace("Ó","O").replace("Ú","U").replace("Ñ","N").replace("Ü","U").casefold()
    lista_texto = texto_usar.split()
    return lista_texto

texto = obtener_texto(texto_usar)
print(texto)
print("\n")
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
print("Lista sin caracteres especiales")
print(eliminar_caracteres(texto))
print("\n")

lista_filtrada_solo_alfabeticos = eliminar_caracteres(texto)
texto
def filtrador(texto):
    #Lista_aux -> Lista que almacenará caracteres de todo el texto (sin caracteres especiales) con >= 5 caracteres, que no se repitan y sean alfabeticos
    lista_aux = []
    for palabra in texto:
        palabra=palabra.lower()
        if len(palabra) >= longitud_minima and not palabra in lista_aux:
            lista_aux.append(palabra)
    return lista_aux
print("Lista con palabras de longitud mayor longitud mínima (5)")
print(filtrador(lista_filtrada_solo_alfabeticos))

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
print("\n")
print(diccionario(lista_filtrada_solo_alfabeticos))

# -------------------------------------------- PARTE 3 ------------------------------------------

diccionario_usar = diccionario(lista_filtrada_solo_alfabeticos)

def validez_longitud():
    longitud = int(input("Ingrese longitud de la palabra que desea adivinar: "))
    while longitud == 0:
        longitud = int(input("Error. Ingrese longitud de la palabra que desea adivinar: "))
    return longitud

longitud_palabra= validez_longitud()

def lista_candidatas(diccionario,longitud):
    lista_candidatas = []
    if longitud >= 5 :
        #Asumiendo que el jugador ingresa alguna longitud  
        print(f"Solo juegan las palabras con {longitud} caracteres\n")
        for clave in diccionario:
            if len(clave) == longitud:
                lista_candidatas.append(clave)
    else:
        #Si no ingresa una longitud o ingresa "cero", juegan todas las palabras
        print("Juegan todas las palabras\n")
        for clave in diccionario:
            lista_candidatas.append(clave)
    return lista_candidatas

print("\n")
print(lista_candidatas(diccionario_usar,longitud_palabra))

palabras_candidatas = lista_candidatas(diccionario_usar,longitud_palabra)

def palabra_aleatoria(lista_candidatas):
    palabraSeleccionada = lista_candidatas[randint(1,len(lista_candidatas)-1)]
    return palabraSeleccionada

print(f"Palabra elegida: {palabra_aleatoria(palabras_candidatas)}")