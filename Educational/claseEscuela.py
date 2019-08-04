from datetime import time, datetime
import operator

def imprimirPorSeparado(lst):
    for i in lst:
        print(i)

listaDeEstudiantes = ['Ana', 'Ingrid', 'Monse', 'Brizeth', 'Carlos', 'Mario', 'Bryan', 'Kimberly', 'Danae', 'Roberto', 'Carolina', 'Perla', 'Angel', 'David', 'Camila', 'Juanpa', 'Azul', 'Yuliza']
dictEstudiantes = {'Monse': datetime(7, 8, 29), 'Brizeth': datetime(9, 7, 5), 'Carlos': datetime(7,6,5), 'Mario': datetime(9,8,5), 'Bryan': datetime(7,2,25), 'Kimberly': datetime(8,7,28), 'Danae': datetime(9,5,2), 'Roberto': datetime(7,6,6), 'Carolina': datetime(9,6,16), 'Perla': datetime(7,3,22), 'Angel':datetime(7,2,12), 'Camila': datetime(8,4,9)}
listaDePresentes = []

def tomarAsistencia():
    for i in listaDeEstudiantes:
        estado = input('¿' + i + ' está presente? ')
        if estado == 'presente':
            listaDePresentes.append(i)
    print()
    print('Presentes:')
    imprimirPorSeparado(listaDePresentes)

def sumarLetras():
    print(sum([len(str) for str in listaDePresentes]))