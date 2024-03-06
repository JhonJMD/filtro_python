import screen as sc
from tabulate import tabulate

def menu():
    sc.cleanScreen()
    header = """
    --------------------------
    |    CONVERTIR MONEDA    |
    --------------------------
    """
    print(header)
    options = [['1','Pesos a Dolares'],['2','Pesos a Euros'],['3','Euros a Pesos'],['4','Pesos a Yenes'],['5','Salir']]
    print(tabulate(options, tablefmt='youtrack'))
    op = input('\n>> ')
    return op

def validacionInt(message : str):
    try:
        val = float(input(message))
    except ValueError:
        print('Dato invalido....')
        sc.pauseScreen()
    else:
        return val
def converter(pesos : float, moneda : float):
    count = 0
    while pesos > 0:
        pesos = pesos-moneda
        count+=1
    return count

def otherConverter(isActiveConverter : bool):
    while True:
        isActiveConverter = input('Desea convertir otro valor: s(si) ---- Enter(no)').upper()
        if isActiveConverter == '':
            isActiveConverter = False
            break 
        elif isActiveConverter == 'S':
            isActiveConverter = True
            break
    return isActiveConverter

isActiveConverter = True
while isActiveConverter:
    op = menu()
    if op == '1':
        sc.cleanScreen()
        moneda = float(3944)
        message = 'Ingrese la cantidad de Pesos Colombianos a convertir: '
        pesos = validacionInt(message)
        result = converter(pesos, moneda)
        print(f'El valor de la conversion es : {result}')
        sc.pauseScreen()
    elif op == '2':
        pass
    elif op == '3':
        pass
    elif op == '4':
        pass
    elif op == '5':
        sc.cleanScreen()
        print('Gracias por utilizar nuestro sistema.....')
        sc.pauseScreen()
    else:
        menu()
    isActiveConverter = otherConverter(isActiveConverter)
