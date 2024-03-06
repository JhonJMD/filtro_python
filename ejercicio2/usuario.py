import screen as sc
from tabulate import tabulate

def validacionInt(message : str):
    while True:
        try:
            val = int(input(message))
        except ValueError:
            print('Dato invalido....')
            sc.pauseScreen()
        else:
            return val

def validacionFloat(message : str):
    while True:
        try:
            val = float(input(message))
        except ValueError:
            print('Dato invalido....')
            sc.pauseScreen()
        else:
            return val  

usuario = {
        'id':0,
        'nombres':'',
        'apellidos':'',
        'ubicacion':{
            'direccion':'',
            'ciudad':'',
            'longitud': 0,
            'latitud': 0
        },
        'email' : '',
        'edad' : 0,
        'ocupacion' : ''
}

id= validacionInt(message='Ingrese el ID del usuario: ')
usuario['id'] = str(id).zfill(3)
usuario['nombres'] = input('Ingrese los nombres del usuario: ')
usuario['apellidos'] = input('Ingrese los apellidos del usuario: ')
usuario['ubicacion']['direccion'] = input('Ingrese la direccion del usuario: ')
usuario['ubicacion']['ciudad'] = input('Ingrese la ciudad del usuario: ')
lon = validacionFloat(message='Ingrese la longitud: ')
usuario['ubicacion']['longitud'] = lon
lat = validacionFloat(message='Ingrese la latitud: ')
usuario['ubicacion']['latitud'] = lat
usuario['email'] = input('Ingrese el email del usuario: ')
edad = validacionInt(message='Ingrese la edad del usuario: ')
usuario['edad'] = edad
usuario['ocupacion'] = input('Ingrese la ocupacion del usuario: ')

sc.cleanScreen()
kys = ['ID','NOMBRE','APELLIDO','UBICACION','EMAIL','EDAD','OCUPACION']
info=[]
for key, value in usuario.items(): 
    value = str(value)
    info.append([value])
print(tabulate([info], headers=kys, tablefmt='fancy_grid'))
sc.pauseScreen()
        