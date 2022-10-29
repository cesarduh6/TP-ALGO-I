def secuenciaRetornoEscape(palabraAhorcado, contadorAciertos, contadorErrores, letras,palabraErronea):
    letra = input("Ingrese una letra (0 o esc salir): ")
    btnEscape, contadorErrores = secuenciaEscape(letra,contadorErrores)
    letraValidar, letras, btnEscape, contadorErrores = ingresosErroneos(letra,letras, contadorErrores)
    
    if letraValidar in palabraAhorcado:
        contadorAciertos += 1
    else:
        contadorErrores += 1
        palabraErronea += letraValidar
    return contadorAciertos,contadorErrores, letras, btnEscape, letraValidar, palabraErronea

def ingresosErroneos(letra,letras,contadorErrores):
    
    bucleErrores = None
    letraValidar = ""
    btnEscape = True

    if len(letra)>1:
        bucleErrores = True
    elif letra.isalpha() == False and letra != "0":
        bucleErrores = True
    elif letra in letras:
        print("letra repetida no cuenta")
        bucleErrores = True
    else:
        letras += letra
        letraValidar = letra
    
    while bucleErrores == True:
        print("Ingreso erroneo")
        letra = input("Ingrese una letra (0 o esc salir): ")
        if letra == "esc" or letra == "0":
            btnEscape, contadorErrores = secuenciaEscape (letra, contadorErrores)
            # print (f" el boton escape dio {btnEscape}, contador errores dio {contadorErrores}")
            bucleErrores = False
        elif len(letra) == 1 and letra.isalpha() == True and letra not in letras:
            letras += letra
            letraValidar = letra
            bucleErrores = False
                
    return letraValidar, letras, btnEscape, contadorErrores

def secuenciaEscape(letra, contadorErrores):
    btnEscape = True
    validacionEscape = False
    
    if letra == "esc" or letra == "0":
        validacionEscape = True

    if validacionEscape == True:
        print("Has escapado")
        btnEscape = False
        contadorErrores = 10
    
    return btnEscape, contadorErrores
    
def mostrarSignosEspeciales(letras, palabraAhorcado):

    muestraParcial = ""

    for i in range (len(palabraAhorcado)):
        if palabraAhorcado[i] in letras:
            muestraParcial += palabraAhorcado[i]
        else:
            muestraParcial += "?"
    print(muestraParcial)

        
    return muestraParcial

def muestraAciertosErrores(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado,palabraErronea):
    
    if letra in palabraAhorcado:
        print(f"Muy bien jajaja {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} ")
    else:
        print(f"Lo siento {muestraParcial} Aciertos: {contadorAciertos} Desaciertos: {contadorErrores} - {palabraErronea}")
    
    return muestraParcial,contadorAciertos, contadorErrores

def ganadorPerdedor(muestraParcial, palabraAhorcado, contadorErrores):

    if muestraParcial == palabraAhorcado:
        contadorErrores = 15
        print("HAS GANADO!")
        
    if contadorErrores == 8:
        print("PERDISTE")

    return contadorErrores

def jugarAhorcado(palabra):
    palabraAhorcado = palabra.lower()
    caracter = "?"
    muestraParcial = len(palabraAhorcado)*caracter
    letras = ""
    palabraErronea = ''
    contadorAciertos = 0
    contadorErrores = 0

    print(f"Palabra a adivinar: {muestraParcial}  Aciertos: {contadorAciertos}  Desaciertos: {contadorErrores}")

    while contadorErrores <= 7:

        contadorAciertos, contadorErrores, letras, btnEscape,letra,palabraErronea = secuenciaRetornoEscape(palabraAhorcado, contadorAciertos, contadorErrores, letras,palabraErronea)

        if btnEscape == True:  

            muestraParcial = mostrarSignosEspeciales(letras,palabraAhorcado)
            muestraParcial, contadorAciertos, contadorErrores = muestraAciertosErrores(letra, muestraParcial, contadorAciertos, contadorErrores, palabraAhorcado,palabraErronea)
            contadorErrores = ganadorPerdedor(muestraParcial, palabraAhorcado, contadorErrores)
            
        else:
            contadorErrores = 100
            
    return None