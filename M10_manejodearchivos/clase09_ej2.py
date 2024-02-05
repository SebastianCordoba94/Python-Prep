import sys
import datetime
import os

tiempo = int(datetime.datetime.timestamp(datetime.datetime.now()))

temperatura = input('Ingrese la temperatura en grados centígrados : ')
humedad = input('Ingrese el porcentaje de humedad : ')
lluvia = input("Ingrese True si llovio / False si no llovio : ")
linea = str(tiempo) + ',' + temperatura + ',' + humedad + ',' + lluvia

logs_lluvia = open('clase09_ej2.csv', 'a')
logs_lluvia.write(linea+'\n')
logs_lluvia.close()
