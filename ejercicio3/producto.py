import screen as sc
import corefile as file

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

def addProduct(productos : dict):
    producto = {
        'id' : 0,
        'nombre' : '',
        'valorUnitario' : 0.0,
        'stockmin' : 0,
        'stockmax' : 0
    }
    if len(productos) == 0:
        id = validacionInt(message='Ingrese el ID del Producto: ')
        producto['id'] = id
    else:
        while True:
            isaddPro = True
            id = validacionInt(message='Ingrese el ID del Producto: ')
            for key in productos.keys():
                if key == str(id):
                    print('Este ID ya se encuentra registrado')
                    isaddPro = False
                    sc.pauseScreen()
            if isaddPro == True:
                producto['id'] = id
                break
    producto['nombre'] = input('Nombre del Producto: ')
    producto['valorUnitario'] = validacionFloat(message='Ingrese el valor unitario del producto: ')
    producto['stockmax'] = validacionInt(message='Ingrese el stock maximo del producto: ')
    producto['stockmin'] = validacionInt(message='Ingrese el stock minimo del producto: ')
    sc.cleanScreen()
    productos.update({id : producto}) #Actualiza el productos con el contenido dado
    file.updateFile('productos.json', productos)

def otherConverter(isActiveConverter : bool):
    while True:
        isActiveConverter = input('Desea convertir otro valor: s(si) ---- Enter(no): ').upper()
        if isActiveConverter == '':
            isActiveConverter = False
            break 
        elif isActiveConverter == 'S':
            isActiveConverter = True
            break
    return isActiveConverter
