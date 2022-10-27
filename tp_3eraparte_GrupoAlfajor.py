from tp_2daparte_GrupoAlfajor import diccionario,lista_filtrada_solo_alfabeticos, longitud_minima
from random import randint

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

print(lista_candidatas(diccionario_usar,longitud_palabra))

palabras_candidatas = lista_candidatas(diccionario_usar,longitud_palabra)

def palabra_aleatoria(lista_candidatas):
    palabraSeleccionada = lista_candidatas[randint(1,len(lista_candidatas)-1)]
    return palabraSeleccionada

"""print(f"Palabra elegida: {palabra_aleatoria(palabras_candidatas)}")"""