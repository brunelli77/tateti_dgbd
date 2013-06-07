# -*- coding: utf-8 -*-
# Tateti por consola ISP20
# License: LGPLv3 (see http://www.gnu.org/licenses/lgpl.html)

# Website - http://www.isp20.edu.ar
import sys
import os
"""os: trae metodos que vos haces con el O.S. (crear carpetas, leer carpetas, hacer archivos, etc)
sys: libreria que nos deja imprimir, etc"""
#armo un diccionario con los sistemas operativos como clave y los comandos
#que borran las consola como valores

comandos = {"posix":"clear","nt":"cls"}

#diccionario con cada una de las posiciones posibles como clave y como valor
#un espacio en blanco que ubicará la marca de cada jugador cuando la elijan
#para colocar su ficha
"""muestra los datos relevantes: tablero (tiene 9 posiciones importantes: puede haber X o 0)
se arma el diccionario clave(posiciones tablero para poner si es X o 0"""
posiciones_tablero={1:" ",2:" ",3:" ",4:" ",5:" ",6:" ",7:" ",8:" ",9:" "}

#dicionario con las fichas de los 2 jugadores, cada ficha tendrá un posición
#asociada, inician en cero los valores, a medida que vayan definiendo posiciones
#se irán almacenando en el correspondiente diccionario y clave-ficha
"""crea un diccionario con las 3 fichas para cada jugador, y tiene dentro OTRO DICCIONARIO"""
fichas_jugadores = {1:{1:0,2:0,3:0},2:{1:0,2:0,3:0}}
"""este diccionario sirve para diferenciar las fichas de cada jugador, el 1 las X y el 2 las 0"""
marcas_jugadores = {1:"X",2:"O"}
"""determina que jugador empieza a jugar y que ficha va a mover (poner en el campo)"""
jugador_actual = 1
ficha_actual = 1

"""arma una funcion"""
def PintarTablero():
    '''utilizo el diccionario con comandos y pasandole la clave que
    retorna os.name que nos dice el sistema operativo en el que estamos'''
    # borra la consola
    """toma el os.name y devuelve el nombre del sistema operativo (posix o nt)"""
    os.system(comandos[os.name])
    for nro in range(1,10):
        #hace una impresion con la libreria sys.stdout.write mediante el FOR, lo hace del 1 al 10(sin el 9)
        sys.stdout.write("[%s]"% posiciones_tablero[nro])
        if (nro%3==0):
            print "\n"
    ##lineas para debug, para poder hacer un seguimiento de la evolución
    ##de los diccionarios
    """print "posiciones_tablero"
    print posiciones_tablero
    print "fichas_jugadores"
    print fichas_jugadores

def Jugar(jugador_actual=0, ficha_actual=0):
    pos_jugada = input("Jugador %i: ingrese posicion para la ficha %i:" % (jugador_actual, ficha_actual))
    fichas_jugadores[jugador_actual][ficha_actual]=pos_jugada
    posiciones_tablero[pos_jugada]=marcas_jugadores[jugador_actual]"""


while True:
    PintarTablero()
    if (ficha_actual==0):
        ficha_actual=input("Jugador %i ingrese el numero de ficha a mover:" % jugador_actual)
    """
    Jugar(jugador_actual, ficha_actual)
    jugador_actual+=1
    if jugador_actual == 3:
        jugador_actual = 1
        ficha_actual+=1
        if ficha_actual == 4:
            ficha_actual = 0
            """
    posicion_elegida = input("Jugador %i: Ingrese la posicion de la ficha %i: " % (jugador_actual, ficha_actual))
    posiciones_tablero[posicion_elegida] = marcas_jugadores[jugador_actual]
    jugador_actual += 1
    if jugador_actual == 3:
        jugador_actual = 1
        ficha_actual += 1
        if ficha_actual == 4:
            ficha_actual = 0