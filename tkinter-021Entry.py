import getpass
import Tkinter

# probar si Tkinter funciona
#

Tkinter._test()
 
from Tkinter import Tk
#from Tkinter import ttk
from Tkinter import *

#creando una funcion adicional
def funcion():
	print("Lo ha logrado")

def femenina():
	print("Sexo femenino")

def masculino():
	print("Sexo masculino")

def curso(datos):
	print(datos)

        
# igual que el anterior pero convirtiendo a float
def palabra(event):
        # toma el valor del primer Entry y lo convierte a entero
        a = ctext1.get()
        b = ctext2.get()
        c = ctext3.get()
        d = ctext4.get()
        palab=a+b+c+d
        resultado.delete(0, "end")
        # devuelve el valor hacia el segundo Entry
        resultado.insert(0,palab)    



# ahora crear el marco contenedor #
raiz = Tk()

# crear titulo #
raiz.title("Primera interfaz grafica usando Python")

# crear componentes en la grid

texto = "Bienvenido al campo de texto"
etiqueta = Label(raiz, text=texto)
etiqueta.pack()


# elementos a leer
etiqueta1 = Label(raiz, text="Aspecto x-(y-n)-xt")
etiqueta1.pack()
ctext1 = Entry(raiz)
ctext1.pack()

etiqueta2 = Label(raiz, text="Objeto in-at-()-oj-ix-e'")
etiqueta2.pack()
ctext2 = Entry(raiz)
ctext2.pack()

etiqueta3 = Label(raiz, text="Sujeto in-a-ru-qa-i-ki")
etiqueta3.pack()
ctext3 = Entry(raiz)
ctext3.pack()

etiqueta4 = Label(raiz, text="Accion")
etiqueta4.pack()
ctext4 = Entry(raiz)
ctext4.pack()


# activacion de la palabra a construir
tiempo = Button(raiz, text="Genera palabra")
tiempo.bind("<Button-1>", palabra)
tiempo.pack()



resultado = Entry(raiz)
resultado.pack()




# correr la composicion #
# en la primera instruccion definimos las dimensiones de la ventana#

raiz.mainloop()

