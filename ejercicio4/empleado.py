import screen as sc
import corefile as file
import menu as m

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

def otherEmpleado(isaddempleado : bool, empleados : dict):
    while True:
        isaddempleado = input('Desea registrar otro empleado: s(si) ---- Enter(no): ').upper()
        if isaddempleado == '':
            isaddempleado = False
            m.menuMain(empleados)
            break 
        elif isaddempleado == 'S':
            isaddempleado = True
            break
    return isaddempleado

def addEmpleado(empleados : dict):
    isaddempleado = True
    while isaddempleado:
        empleado = {
            'id' : 0,
            'nombre' : '',
            'cargo' : '',
            'salario' : 0
        }
        if len(empleados) == 0:
            id = validacionInt(message='Ingrese el ID del Empleado: ')
            empleado['id'] = id
        else:
            while True:
                isaddEm = True
                id = validacionInt(message='Ingrese el ID del Empleado: ')
                for key in empleados.keys():
                    if key == str(id):
                        print('Este ID ya se encuentra registrado')
                        isaddEm = False
                        sc.pauseScreen()
                if isaddEm == True:
                    empleado['id'] = id
                    break
        empleado['nombre'] = input('Nombre del Empleado: ')
        empleado['cargo'] = input('Ingrese el cargo del empleado (Almacenista, Jefe IT, Administrador, Mensajero, Gerente)')
        sc.cleanScreen()
        empleados.update({id : empleado}) #Actualiza el empleados con el contenido dado
        file.updateFile('empleados.json', empleados)
        isaddempleado = otherEmpleado(isaddempleado, empleados)

def calcularVal(empleados : dict, nomina : dict):
    idP = 0
    isaddempleado = True
    while isaddempleado:
        pagado = {
            'idP' : 0,
            'diasTrabajados' : 0.0,
            'horasExtras' : 0.0,
            'valorDia' : 0.0,
            'descuentoCafeteria' : 0.0,
            'cuotaPrestamo' : 0.0
        }
        if len(empleados) == 0:
            print('No hay ningun empleado registrado')
            sc.pauseScreen()
        else:
            idP+=1
            id = validacionInt(message='Ingrese el id del empleado a calcular: ')
            for key in empleados.keys():
                if key == str(id):
                    pagado['diasTrabajados'] = validacionFloat(message='Ingrese los dias trabajados: ')
                    pagado['horasExtras'] = (validacionFloat(message='Ingrese el valor del dia: ')*5500)
                    pagado['descunetoCafeteria'] = validacionFloat(message='Ingrese el valor de descuento por cafeteria: ')
                    pagado['cuotaPrestamo'] = validacionFloat(message='Ingrese la cuota de descuento: ')
                    sc.cleanScreen()
                    nomina.update({idP : pagado}) #Actualiza el nomina con el contenido dado
                    file.updateFile('nomina.json', nomina)
                    isaddempleado = otherEmpleado(isaddempleado, nomina)
                    
            