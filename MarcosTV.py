import tkinter
import webbrowser
ventana = tkinter.Tk()
ventana.geometry("1920x1080")

def test():
   webbrowser.open_new_tab('Test.html')

boton1 = tkinter.Button(ventana,text ="WEB", width = 10, height=5, command = test );
boton2 = tkinter.Button(ventana,text ="boton2", width = 10, height=5);
boton3 = tkinter.Button(ventana,text ="boton3", width = 10, height=5);


boton1.grid(row = 3, column = 0)
boton2.grid(row = 4, column = 0)
boton3.grid(row = 5, column = 0)

ventana.mainloop()


