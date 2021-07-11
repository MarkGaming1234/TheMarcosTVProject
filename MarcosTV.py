import Tkinter as tk
from PIL import ImageTk, Image
import os

ventana = tkinter.Tk()
ventana.geometry("1920x1080")

img= ImageTK.PhotoImage(Image.open("Fondo.jpg"))

etiqueta = tkinter.Label(ventana, image =img)
boton1 = tkinter.Button(ventana,text ="boton1", width = 10, height=5);
boton2 = tkinter.Button(ventana,text ="boton2", width = 10, height=5);
boton3 = tkinter.Button(ventana,text ="boton3", width = 10, height=5);

etiqueta.pack()
boton1.grid(row = 3, column = 0)
boton2.grid(row = 4, column = 0)
boton3.grid(row = 5, column = 0)

ventana.mainloop()


