import screen as sc
import empleado as em
from tabulate import tabulate

def menuMain(empleados : dict, nomina : dict, colillas : dict):
    sc.cleanScreen()
    header = """
    --------------------------
    |         NOMINA         |
    --------------------------
    """
    print(header)
    options = [['1','Gestor Empleados'],['2','Total pagado por concepto de nomina'],['3','Consulta Colilla de pago'],['4','Salir']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if op == '1':
        sc.cleanScreen()
        menuEmpleados(empleados, nomina)
    elif op == '2':
        pass
    elif op == '3':
        pass
    elif op == '4':
        print('Gracias por utilizar nuestro sistema......')
        sc.pauseScreen()
    else:
        menuMain(empleados)

def menuEmpleados(empleados : dict, nomina : dict):
    sc.cleanScreen()
    header = """
    --------------------------
    |    GESTOR EMPLEADOS    |
    --------------------------
    """
    print(header)
    options = [['1','Registrar Empleados'],['2','Calcular valor a pagar'],['3','Colilla de pago'],['4','Salir']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    if op == '1':
        sc.cleanScreen()
        em.addEmpleado(empleados)
    elif op == '2':
        sc.cleanScreen()
        em.calcularVal(empleados, nomina)
    elif op == '3':
        pass
    elif op == '4':
        menuMain(empleados)
    else:
        menuEmpleados(empleados)