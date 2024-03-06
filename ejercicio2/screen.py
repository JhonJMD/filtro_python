import sys
import os

def cleanScreen():
    if sys.platform == 'linux':
        os.system('clear')
    else:
        os.system('cls')

def pauseScreen():
    if sys.platform == 'linux':
        input('Presione cualquier tecla para continuar.......')
    else:
        os.system('pause')