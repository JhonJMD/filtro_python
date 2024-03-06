import sys
import os

def cleanScreen():
    if sys.platform == 'linux':
        os.system('clean')
    elif sys.platform == 'win32':
        os.system('cls')

def pauseScreen():
    if sys.platform == 'linux':
        input('Presione cualquier tecla para continuar.......')
    elif sys.platform == 'win32':
        os.system('pause')