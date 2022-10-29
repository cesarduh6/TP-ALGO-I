def puntajes(letra, palabraAhorcado, muestraParcial, contadorErrores):
    puntaje = 0
    while (letra != "0" or letra != "esc") or (muestraParcial != palabraAhorcado) or (contadorErrores <=7):
        if letra in palabraAhorcado:
            puntaje += 10
        else:
            puntaje -=5
    return puntaje