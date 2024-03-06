import os 
import json

BASE = 'ejercicio4/data/'
#Chequear si el archivo json existe y si no existe lo crea
#Recibe: el nombre del archivo
def checkFile(file : str): 
    if not os.path.isfile(BASE+file):
        with open(BASE+file, 'w') as create_file:
            json.dump({}, create_file, indent = 4)  
    else: 
        pass

#Lee el archivo y lo carga a una variable dada en otra función
#Recibe: Nombre del archivo
#Retorna: El contenido del archivo cargado
def readFile(file : str):
    with open(BASE+file, 'r') as read_file:
        return json.load(read_file)

#Actualiza el archivo con el contenido dado
#Recibe: Nombre del archivo, contenido a actualizar
def updateFile(file : str, contenido):
    with open (BASE+file, 'w+') as update_file:
        json.dump(contenido, update_file, indent = 4)