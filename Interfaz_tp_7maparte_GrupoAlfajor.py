import csv
from tkinter import *
from tkinter import messagebox


def creacion_ventana_de_inicio():
    #Esta funcion crea la ventana principal(la gris oscura)
    global ventana_principal
    ventana_principal=Tk()
    ventana_principal.title("Login Alfajor")
    ventana_principal.resizable(0,0)
    ventana_principal.geometry("280x180")
    ventana_principal.iconbitmap("descarga.ico")
    ventana_principal.config(background="gray")
    global usuario
    global clave
    usuario = StringVar()
    clave = StringVar()
    global entrada_usuario
    global entrada_clave
    #Label "Comentario de Bienvenida"
    comentario1 = Label(text = "Bienvenido al juego del Ahorcado")
    comentario1.pack()
    comentario1.place(x=30, y=20)
    comentario1.config(background="LightGreen")
    #Label "Usuario"
    usuario_a_ingresar= Label(text = "Usuario Jugador: ")
    usuario_a_ingresar.pack()
    usuario_a_ingresar.place(x=10, y=70)
    #Label "Clave"
    clave_a_ingresar= Label(text = "Clave: ")
    clave_a_ingresar.pack()
    clave_a_ingresar.place(x=10,y=100)
    #Caja de texto para Usuario
    entrada_usuario = Entry(ventana_principal,textvariable=usuario)
    entrada_usuario.pack()
    entrada_usuario.place( x=120, y=70)
    #Caja de texto para Clave
    entrada_clave = Entry(ventana_principal,textvariable=clave)
    entrada_clave.place( x=120, y=100)
    entrada_clave.config(show="*")
    #Boton Ingresar
    boton_ingresar = Button(ventana_principal,text="Ingresar",command = validar_usuario_nombre_y_clave_registrado)
    boton_ingresar.pack()
    boton_ingresar.place(x=30,y=140)
    #Boton Iniciar partida
    boton_iniciar_partida = Button(ventana_principal,text="Iniciar partida")
    boton_iniciar_partida.pack()
    boton_iniciar_partida.place(x=90,y=140)
    #Boton Registrarse
    boton_registrarse = Button(ventana_principal,text="Registrarse",command = registro_de_jugador)
    boton_registrarse.pack()
    boton_registrarse.place(x=180,y=140)

    ventana_principal.mainloop()

    

def registro_de_jugador():
    #Esta funcion crea la ventana registro de jugador
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x280")
    global nombre_usuario_new
    global clave_new
    global clave_new_bis
    nombre_usuario_new= StringVar() 
    clave_new= StringVar() 
    clave_new_bis=StringVar()
    global entrada_nombre_usuario_nuevo
    global entrada_clave_nueva
    global entrada_clave_nueva_otra_vez
    #Label "Usuario_nuevo"
    etiqueta_usuario_nuevo = Label(ventana_registro,text = "Ingrese nombre: ")
    etiqueta_usuario_nuevo.pack()
    etiqueta_usuario_nuevo.place(x=10, y=20)
    #Label "Clave_nueva"
    clave_nueva = Label(ventana_registro,text = "Ingrese una Clave: ")
    clave_nueva.pack()
    clave_nueva.place(x=10,y=100)
    #Label "Pedido clave nueva otra vez"
    clave_nueva_otra_vez= Label(ventana_registro,text = "Ingresela otra vez: ")
    clave_nueva_otra_vez.pack()
    clave_nueva_otra_vez.place(x=10,y=180)
    #Caja de texto para Usuario-nuevo
    entrada_nombre_usuario_nuevo = Entry(ventana_registro,textvariable=nombre_usuario_new)
    entrada_nombre_usuario_nuevo.pack()
    entrada_nombre_usuario_nuevo.place( x=120, y=20)
    #Boton en caja de texto para nombre de usuario nuevo
    boton_entrada_usuario_nuevo = Button(ventana_registro,text="Hecho",command=validar_entrada_nombre_usuario_nuevo)
    boton_entrada_usuario_nuevo.pack()
    boton_entrada_usuario_nuevo.place(x=150,y=50)
    #Caja de texto para Clave_nueva
    entrada_clave_nueva = Entry(ventana_registro,textvariable=clave_new)
    entrada_clave_nueva.pack()
    entrada_clave_nueva.place( x=120, y=100)
    entrada_clave_nueva.config(show="*")
    #Boton en caja de texto para clave de usuario nuevo
    boton_entrada_clave_nueva = Button(ventana_registro,text="Hecho",command=validar_entrada_clave_nueva)
    boton_entrada_clave_nueva.pack()
    boton_entrada_clave_nueva.place(x=150,y=130)
    #Caja de texto para Clave_nueva otra vez
    entrada_clave_nueva_otra_vez= Entry(ventana_registro,textvariable=clave_new_bis)
    entrada_clave_nueva_otra_vez.pack()
    entrada_clave_nueva_otra_vez.place( x=120, y=180)
    entrada_clave_nueva_otra_vez.config(show="*")
    #Boton en caja de texto para clave  ingresada otra vez de usuario nuevo
    boton_entrada_clave_nueva = Button(ventana_registro,text="Hecho",command=validar_entradas_claves_nuevas)
    boton_entrada_clave_nueva.pack()
    boton_entrada_clave_nueva.place(x=150,y=200)
    #Boton Crear Usuario Nuevo Completo
    boton_usuario_nuevo= Button(ventana_registro,text="Registrarse",command = lambda:registro_usuarios_nuevos(nombre_usuario_new.get(), clave_new.get()))
    boton_usuario_nuevo.pack()
    boton_usuario_nuevo.place(x=100,y=250)



def validar_nombre_jugador_nuevo():
    #Esta funcion valida el nombre del usuario nuevo que quiere registrase(si tiene entre 4 o 15 caracteres,si tiene guion,letra y nuemro)
    info_nombre_usuario_nuevo=nombre_usuario_new.get()
    posicion=0
    longitud_minima=4
    longitud_maxima=15
    guion=False
    letra=False
    numero=False
    if longitud_minima <= len(info_nombre_usuario_nuevo) <= longitud_maxima:
        while(posicion < len(info_nombre_usuario_nuevo)):
            if (info_nombre_usuario_nuevo[posicion] == "_"):
                guion=True
            elif (info_nombre_usuario_nuevo[posicion].isalpha()):
                letra=True
            elif (info_nombre_usuario_nuevo[posicion].isnumeric()):
                numero=True
            posicion = posicion + 1
    return guion and letra and numero
    


        
def validar_clave_de_jugador_nuevo():
    #Esta funcion valida la clave nueva del usuario nuevo(si tiene mayus,munus,numero,simbolo valido y no simbolos invalidos)
    info_clave_usuario_nuevo=str(clave_new.get())
    hay_mayuscula = False
    hay_minuscula = False
    tiene_digito = False
    tiene_simbolo_valido = False
    tiene_simbolo_invalido = False
    long_minima = 8
    long_maxima = 12
    posicion = 0
    if long_minima <= len(info_clave_usuario_nuevo) <= long_maxima:
         while (posicion < len(info_clave_usuario_nuevo) and (not info_clave_usuario_nuevo[posicion] in ['Á','É','Í','Ó','Ú','á','é','í','ó','ú']) and not tiene_simbolo_invalido):
            if info_clave_usuario_nuevo[posicion].isupper():
                hay_mayuscula = True
            elif info_clave_usuario_nuevo[posicion].islower():
                hay_minuscula = True
            elif info_clave_usuario_nuevo[posicion].isdigit():
                tiene_digito = True
            elif info_clave_usuario_nuevo[posicion] in ['-','_']:
                tiene_simbolo_valido = True
            else:
                tiene_simbolo_invalido = True
            posicion = posicion + 1
    return hay_mayuscula and hay_minuscula and tiene_digito and tiene_simbolo_valido and not tiene_simbolo_invalido



def validar_entrada_nombre_usuario_nuevo():
    #Esta funcion valida si el nombre del usuario esta ya registrado (leyendo el archivo registracion), si no es blanco anteriormente y manda mensajes
    info_nombre_usuario_nuevo=nombre_usuario_new.get()
    usuario_a_registrar=False
    linea=" "
    validacion_entrada_nombre_usuario_nuevo=validar_nombre_jugador_nuevo()
    if info_nombre_usuario_nuevo != "":
        archivo=open("registracion.csv", "r")
        linea=archivo.readline()
        while linea != "" and (not usuario_a_registrar):
            linea=archivo.readline()
            linea_convertida_a_lista= linea.rstrip("\n").split(",")
            print(linea_convertida_a_lista[0] ,info_nombre_usuario_nuevo )
            if linea_convertida_a_lista[0] == info_nombre_usuario_nuevo:
                usuario_a_registrar=True
                messagebox.showerror(message="Nombre de Usuario no valido. Ya existe.")
                entrada_nombre_usuario_nuevo.delete(0,END)
        if not validacion_entrada_nombre_usuario_nuevo:
            messagebox.showerror(message="El usuario no existe pero es invalido (tiene que tener una letra,un numero y un guion")
            entrada_nombre_usuario_nuevo.delete(0,END)
        else:
            messagebox.showinfo(message="El nombre no exiSte y es valido.Ingrese la clave")
        archivo.close()
    else:
        messagebox.showerror(message="El nombre no puede estar en blanco")
        
            
        
def validar_entrada_clave_nueva():
    validacion_entrada_clave_usuario_nuevo_valido=validar_clave_de_jugador_nuevo()
    info_clave_usuario_nuevo=str(clave_new.get())
    if info_clave_usuario_nuevo != " ":
        if not validacion_entrada_clave_usuario_nuevo_valido:
            messagebox.showerror(message="Clave invalida")
            entrada_clave_nueva.delete(0,END)
        else:
            messagebox.showinfo(message="clave valida,Continue") 
    else:
        messagebox.showerror(message="La clave no puede estar en blanco")
           


    


def validar_usuario_nombre_y_clave_registrado():
    #Esta funcion valida en la ventana principal si el usuario pone el nombre y clave correctos(si ya esta registardo),abriendo el archivo registracion.csv y leyendolo
    nombre_usuario_registrado=usuario.get()
    clave_usuario_registrado=str(clave.get())
    usuario_registrado=False
    clave_registrada=False
    linea=" "
    if nombre_usuario_registrado != "" and clave_usuario_registrado != "":
        archivo=open("registracion.csv", "r")
        while linea != "" and (not usuario_registrado):
            linea=archivo.readline()
            if linea != "":
                usuario_linea, clave_linea = linea.rstrip("\n").split(",")
                usuario_registrado=False
                clave_registrada=False
                if usuario_linea == nombre_usuario_registrado:
                    usuario_registrado=True
                    if clave_linea == clave_usuario_registrado:
                        clave_registrada=True
            else:
                linea=""
        archivo.close()
        if usuario_registrado and clave_registrada:
            ingresar_usuarios_a_la_sala_de_juego(nombre_usuario_registrado)
            messagebox.showinfo(message="El usuario y la clave son correctos, puede jugar")
            entrada_usuario.delete(0,END)
            entrada_clave.delete(0,END)
        elif not usuario_registrado:
            messagebox.showerror(message="El Usuario no existe. Ingrese el nombre correcto o Regístrese.")
        elif not clave_registrada:
            messagebox.showerror(message="La clave es incorrecta. Ingrese el Usuario y la Clave nuevamente.")
    else:
        messagebox.showerror(message="Nombre de Usuario y/o Clave no validos. No pueden estar en blanco.")
    entrada_usuario.delete(0,END)
    entrada_clave.delete(0,END)





def ingresar_usuarios_a_la_sala_de_juego(nombre_jugador):
    #Esta funcion (cuando todo esta bien validado) guarda el nombre del usuario en un archivo csv y a mediada que ingresan mas jugadores se sigue guardando
    lista_jugador=[nombre_jugador]
    with open("Ingresos.csv","a",newline="") as file:
        writer=csv.writer(file,delimiter=",")
        writer.writerow(lista_jugador)
    contador=0
    with open("Ingresos.csv", "r",newline="") as file:
        linea = file.readline()
        while linea != '':
            contador=contador + 1
            linea = file.readline()
            if contador == 5:
                messagebox.showinfo(message="Recuerde que solo se permite el ingreso de hasta 4 jugadores")
                usuario(state=DISABLED)
    




def validar_entradas_claves_nuevas():
    #Esta funcion valida en la venta de registro de jugador si la clave ingresada(validada anteriormente) y la misma clave ingresada otra vez es igual 
    info_clave_usuario_nuevo=str(clave_new.get())
    info_clave_usuario_nuevo_bis=str(clave_new_bis.get())
    if info_clave_usuario_nuevo != info_clave_usuario_nuevo_bis:
        messagebox.showerror(message="Las claves ingresadas no coinciden")
        entrada_clave_nueva_otra_vez.delete(0,END)
    else:
        messagebox.showinfo(message="Las claves coinciden,continue")


def registro_usuarios_nuevos(datos_nombre_usuario_nuevo,datos_clave_usuario_nuevo):
    #Esta funcion (cuando todo esta bien validado) guarda los datos del usuario nuevo en un archivo llamado registracion.csv e imprime arriba "registro completado con exito"
    datos_usuario_nuevo=[datos_nombre_usuario_nuevo,datos_clave_usuario_nuevo]
    with open("registracion.csv","a",newline="") as file:
        writer=csv.writer(file,delimiter=",")
        writer.writerow(datos_usuario_nuevo)
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
    entrada_nombre_usuario_nuevo.delete(0,END)
    entrada_clave_nueva.delete(0,END)
    entrada_clave_nueva_otra_vez.delete(0,END)

print(creacion_ventana_de_inicio())

