import corefile as file
import menu as m

file.checkFile('empleados.json')
empleados = file.readFile('empleados.json')
file.checkFile('nomina.json')
nomina = file.readFile('nomina.json')
file.checkFile('colillas.json')
colillas = file.readFile('colillas.json')

m.menuMain(empleados, nomina, colillas)

