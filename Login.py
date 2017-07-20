#!/usr/bin/env python3
"""
@author: ISC juan luis Ordoñez perez
"""
import tkinter as tk #importamos la lo libreria que nos permitira hacer una grafica
from tkinter import messagebox

def validar():
    if entrada1.get()=='lili':
        abrirventana2()
    else:
        messagebox.showwarning("cuidado","password incorrecto")

def abrirventana2():
    ventana.withdraw()
    win=tk.Toplevel()
    win.geometry('380x300')
    win.configure(background='dark turquoise')
    e3=tk.Label(win,text="Bienvenid@ a la segunda ventana",bg="gray",fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=tk.X)
    
    boton2=tk.Button(win,text='ok',command=win.destroy)
    boton2.pack(side=tk.TOP)

def cerrarventana():
    ventana.destroy()
#empieza la parte grafica

ventana=tk.Tk()
ventana.title("LOGING")
#anchoxalto en pixeles
ventana.geometry('380x300')
#color de fondo de la ventana
ventana.configure(background='dark turquoise')


e1=tk.Label(ventana,text="password:",bg="gray",fg="white")
e1.pack(padx=5,pady=5,ipadx=5,ipady=5)

entrada1=tk.Entry(ventana)#donde el usuario escribe su contraseña
entrada1.pack(fill=tk.X,padx=5,pady=5,ipadx=5,ipady=5)


boton=tk.Button(ventana,text="Nueva ventana",fg="blue",command=abrirventana2)
boton.pack(side=tk.TOP)

boton3=tk.Button(ventana,text="validar password",fg="blue",command=validar)
boton3.pack(side=tk.TOP)

boton4=tk.Button(ventana,text="Cerrar Ventana",fg="blue",command=cerrarventana)
boton4.pack(side=tk.TOP)

ventana.mainloop()
