#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys
import time
print("------------------------------------------------------------------------------")
print('¡Hola! ¿Cómo te llamas?')
print("------------------------------------------------------------------------------")
miNombre = input()
while miNombre == "":
    print("------------------------------------------------------------------------------")
    print('Porfavor escriba un nombre')
    print("------------------------------------------------------------------------------")
    miNombre = input()
print("------------------------------------------------------------------------------")
print('Bueno, ' + miNombre + ', estoy pensado en 4 números seguidos, eres capaz de adivinarlos?')
print('Responda, si o no')
print("------------------------------------------------------------------------------")
respuesta=input()
respuesta=respuesta.lower()
while respuesta != 'si' and respuesta != 'no' :
    print("------------------------------------------------------------------------------")
    print('Porfavor responda, si o no')
    print("------------------------------------------------------------------------------")
    respuesta=input()
    respuesta=respuesta.lower()
if respuesta == "no":
    print("------------------------------------------------------------------------------")
    print("Bueno otro día será, Adiós")
    print("------------------------------------------------------------------------------")
    input("Pulsa una tecla para cerrar...")
elif respuesta == "si":
    print("------------------------------------------------------------------------------")
    print("Tienes 10 intentos para adivinar mis números")
    print('Intento número 1: introduce 4 números')
    print("------------------------------------------------------------------------------")
    numusuari=input()
    while len(numusuari) != 4 or not numusuari.isdigit():
        print("------------------------------------------------------------------------------")
        numusuari=input("Porfavor escriba 4 dígitos seguidos: ")
        print("------------------------------------------------------------------------------")
    numero=random.randint(1000,9999)
    print (numero)
    numero=str(numero)
    numusuari=str(numusuari)
    contador=1
    intentos=10
    while numusuari != numero :
        aciertos=0
        resultado=""
        for i in range(4):
            if numusuari[i] == numero[i]:
                aciertos=aciertos+1
                resultado=resultado+numero[i]
            else:
                resultado=resultado+"X"
        if intentos == 1:
            print("------------------------------------------------------------------------------")
            print("Uyy, se te han acabado los intentos amigo")
            print("El número era: "+numero)
            print("Esta vez no tuviste suerte, hasta la próxima")
            print("------------------------------------------------------------------------------")
            input("Pulsa una tecla para cerrar...")
            sys.exit()
        if aciertos == 0:
            intentos=intentos-1
            contador=contador+1
            print("------------------------------------------------------------------------------")
            print("Que pena, no has acertado ningún número de los 4 que estoy pensando")
            print("Te quedan "+str(intentos)+" intentos")
            print("------------------------------------------------------------------------------")
        elif aciertos == len(str(1)):
            intentos=intentos-1
            contador=contador+1
            print("------------------------------------------------------------------------------")
            print("Has acertado 1 número de los 4 que estoy pensando")
            print("Te doy una pista: "+ resultado)
            print("Te quedan "+str(intentos)+ " intentos")
            print("------------------------------------------------------------------------------")
        else:
            intentos=intentos-1
            contador=contador+1
            print("------------------------------------------------------------------------------")
            print("Has acertado"+ " " + str(aciertos) +" " + "números de los 4 que estoy pensando")
            print("Te doy una pista: "+ resultado)
            print("Te quedan "+str(intentos)+ " intentos")
            print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        numusuari=input("Intento número: "+str(contador)+" Prueba de nuevo: ")
        print("------------------------------------------------------------------------------")
        while len(numusuari) != 4 or not numusuari.isdigit():
            print("------------------------------------------------------------------------------")
            numusuari=input("Porfavor escriba 4 dígitos seguidos: ")
            print("------------------------------------------------------------------------------")

    #SI SE ACIERTA EL NÚMERO
    calculo=11-intentos
    calculo2=intentos-1
    fecha=time.strftime("%d/%m/%y")
    hora=time.strftime("%X")
    print ("----------------------------------------")
    print ("!!!! HENORABUENA LO HAS ACERTADO !!!")
    print ("----------------------------------------")
    print ("----------------------------------------")
    print ("ESTADÍSTICAS DEL "+fecha+" A LAS "+hora)
    print ("----------------------------------------")
    print ("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    print ("----------------------------------------")
    print ("NOMBRE: "+miNombre.upper())
    print ("NUMERO ACERTADO: "+numero)
    print ("ACERTADO EN "+str(calculo)+" INTENTOS")
    print ("----------------------------------------")
    input("Pulsa una tecla para cerrar...") 
