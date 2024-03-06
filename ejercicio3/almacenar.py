import corefile as file
import producto as p

file.checkFile('productos.json')
productos = file.readFile('productos.json')

p.addProduct(productos)