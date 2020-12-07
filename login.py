#!/usr/bin/python

import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

root=tk.Tk()
root.title("Login")
root.resizable(0,0)
root.geometry("250x400")

# configuracion de la ventana y iconos
imgen_login=PhotoImage(file="avatar.png")
# tipo de letra
tipo_letra="Arial 12 "
# varibales
usuario=tk.StringVar()
password=tk.StringVar()
new_usuario=tk.StringVar()
new_password=tk.StringVar()

def New_cuenta(): # cremos cuenta nueva
    n_u=new_usuario.get()
    n_p=new_password.get()

    f=open(n_u,"w") # abrimos un txt con el nombre usuario
    f.write(str(n_u) + "\n" + str(n_p)) # colocamos adentro usuario,password
    f.close() # cerramos
    messagebox.showinfo("Cuenta","Cuenta creada con exito") # informamos que todo esta bien

def New_user():
    root2=Toplevel(root) # creamos otra ventana
    root2.title("Nueva cuenta")
    root2.resizable(0,0)
    root2.geometry("230x170")
    etiketa_new_usuario=tk.Label(root2, text="Usuario").place(x=30,y=20)
    etiketa_new_usuario=tk.Entry(root2, textvariable=new_usuario).place(x=30,y=40)
    etiketa_new_password=tk.Label(root2, text="password").place(x=30,y=70)
    etiketa_new_password=tk.Entry(root2, textvariable=new_password).place(x=30,y=90)
    etiketa_boton_guardar=tk.Button(root2, text="crear",command=New_cuenta).place(x=80,y=120)

def Com_user(): # comprobar usuario
    u=usuario.get()
    p=password.get()
    try:  # si se encuentra archivo con nombre de usuario ejecutar lo de abajo
        comprobar=open(u)
        for line in comprobar.readlines():
            comprobar=line.strip("\n")
            if (comprobar==p):
                messagebox.showinfo("Entrar","Usuario correcto")
                print ("[*] Usuario correcto")
                print ("[*] Contraseña correcta")
    except: # si no se encuentra imprimir
        print ("[-] Usuario no encontrado")

def User():
    icono_imagen=tk.Label(root, image=imgen_login).place(x=35,y=20)
    etiketa_usuario=tk.Label(root, text="Usuario",font=tipo_letra).place(x=90,y=210)
    etiketa_usuario=tk.Entry(root, textvariable=usuario).place(x=40,y=235)
    etiketa_password=tk.Label(root, text="Password",font=tipo_letra).place(x=90,y=265)
    etiketa_password=tk.Entry(root, textvariable=password).place(x=40,y=295)
    boton_entrar=tk.Button(root, text="Entrar",command=Com_user).place(x=90,y=325)
    boton_crear_cuenta=tk.Button(root, text="Crear cuenta",font=("root",8),border=0,command=New_user).place(x=140,y=365)    

if __name__=="__main__":
    User()

root.mainloop()