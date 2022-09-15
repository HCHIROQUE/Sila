#Importamos la librería random
from random import randint, choice
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Primero Mostraremos la trivia en la pantalla
print(BLUE + "--------------------------------------------------------------" +
      RESET)
print(BLUE + "Bienvendo a la trivia, sobre preguntas de la HISTORIA DEL PERÚ" +
      RESET)
print(BLUE + "--------------------------------------------------------------" +
      RESET)
nameUser = input("\tEscribe tu nombre: ")

#Personalizamos el juego, preguntando su nombre
print(
    "\nAmigo " + BLUE + nameUser.upper() + RESET +
    ",si estás aquí es porque quieres poner a prueba tus conocimientos... Cada respuesta correcta tiene 10 pts, y cada incorrecta te restará 10 pts,..Diviértete! 😎\n"
)

#Instrucciones del juego
print(
    BLUE + nameUser.upper() + RESET +
    ",responde a las siguientes peguntas, escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta: 📖🖱"
)

#Carga inical de segundos
#tiempoEspera = randint(0,2)

for tiempoEspera in range(0, 2):
    time.sleep(5)

#Lista de puntajes
lista_puntaje_por_intentos = []

#Iniciamos la trivia pa que jueguen
iniciar_trivia = True

#Número de intentos que el jugador intenta nuestra trivia
intentos = 0

#Vamos a implementar el puntaje para que sea divertido
puntaje = randint(0, 11)

while iniciar_trivia == True:

    intentos += 1
    puntaje = randint(0, 11)

    print(MAGENTA + "\nComenzarás con " + str(puntaje) + " punto(s)." + RESET)

    for tiempoEspera in range(0, 1):
        time.sleep(5)

    #1ra pregunta --------------------------------------------------------------
    lista_p1 = [
        "a) 30 Octubre 2017", "b) 15 Septiembre 2016", "c) 23 Noviembre 2015",
        "d) 7 Agosto 2018"
    ]
    print(
        BLUE +
        "\n1.¿Cuál es la fecha en que se lanzó el 1er satélite peruano al espacio?"
        + RESET)
    for elementsp1 in lista_p1:
        print(elementsp1)

    respuesta_p1 = input("¿Cúal es tu respuesta?: ")

    while respuesta_p1 not in ("a", "b", "c", "d"):
        respuesta_p1 = input(
            "Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_p1 == "b":
        puntaje += randint(0, 51)

        print(GREEN + "-----------------------------------------------" +
              RESET)
        print(GREEN + "|Muy bien " + nameUser.upper() + ", mi parcee!!!" +
              RESET)
        print(GREEN + "------------------------------------------------" +
              RESET)
    else:
        puntaje -= randint(0, 11)

        print(RED + "-------------------------------" + RESET)
        print(RED + "|Casi bro, intenta de nuevo...|" + RESET)
        print(RED + "-------------------------------" + RESET)

    print("\t\t\tTu puntaje actual es: ", BLUE + str(puntaje) + RESET)

    time.sleep(3)

    #2da pregunta -----------------------------------------------------------------
    lista_p2 = [
        "a) PerúCND-0", "b) PerúTAS-0", "c) PerúSAT-1", "d) PerúCHASQUI-1"
    ]
    print(BLUE + "\n\n2.¿Cómo se llamó el primer satélite peruano?" + RESET)
    for elementsp2 in lista_p2:
        print(elementsp2)

    respuesta_p2 = input("¿Cúal es tu respuesta?: ")

    while respuesta_p2 not in ("a", "b", "c", "d", "v"):
        respuesta_p2 = input(
            "Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_p2 == "a":
        puntaje -= randint(0, 11)

        print(RED + "--------------------------------------------------" +
              RESET)
        print(RED + "Incorrecto, " + nameUser.upper() +
              ". PerúCND-0 no existe." + RESET)
        print(RED + "--------------------------------------------------" +
              RESET)
    elif respuesta_p2 == "b":
        puntaje -= randint(0, 11)

        print(RED + "--------------------------------------------------" +
              RESET)
        print(RED + "Incorrecto, " + nameUser.upper() +
              ". PerúTAS-0 no existe." + RESET)
        print(RED + "--------------------------------------------------" +
              RESET)
    elif respuesta_p2 == "d":
        puntaje -= randint(0, 11)

        print(RED + "------------------------------------------------------" +
              RESET)
        print(RED + "Incorrecto, " + nameUser.upper() +
              ". PerúCHASQUI-1 no existe." + RESET)
        print(RED + "------------------------------------------------------" +
              RESET)
    elif respuesta_p2 == "v":
        puntaje += 10000

        print(
            MAGENTA +
            "-------------------------------------------------------------------------"
            + RESET)
        print(
            MAGENTA +
            "Este es un mensaje secretito :3 . Y por descubrirlo obtendrás 10000 puntos!!"
            + RESET)
        print(
            MAGENTA +
            "-------------------------------------------------------------------------"
            + RESET)
    else:
        puntaje += randint(0, 31)

        print(GREEN + "------------------------" + RESET)
        print(GREEN + "|Muy bien " + nameUser.upper() + ", mi parcee!!!|" +
              RESET)
        print(GREEN + "------------------------" + RESET)

    print("\t\t\tTu puntaje actual es: ", BLUE + str(puntaje) + RESET)
    time.sleep(3)

    #3ra pregunta ------------------------------------------------------------------
    lista_p3 = ["a) 1879", "b) 1789", "c) 1897", "d) 1798"]
    print(BLUE + "\n\n3.¿En que año fue la guerra de Perú vs. Chile?" + RESET)
    for elementsp3 in lista_p3:
        print(elementsp3)

    respuesta_p3 = input("¿Cúal es tu respuesta?: ")

    while respuesta_p3 not in ("a", "b", "c", "d"):
        respuesta_p3 = input(
            "Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_p3 == "a":
        puntaje += randint(0, 41)

        print(GREEN + "-------------------------------------" + RESET)
        print(GREEN + "|Muy bien " + nameUser.upper() + ", mi parcee!!!|" +
              RESET)
        print(GREEN + "-------------------------------------" + RESET)
    else:
        puntaje -= randint(0, 11)

        print(RED + "-------------------------------" + RESET)
        print(RED + "|Casi bro, intenta de nuevo...|" + RESET)
        print(RED + "-------------------------------" + RESET)

    print("\t\t\tTu puntaje actual es: ", BLUE + str(puntaje) + RESET)
    time.sleep(3)

    #4ta pregunta-----------------------------------------------------------------------
    lista_p4 = ["a) 1820", "b) 1821", "c) 1875", "d) 1921"]
    print(BLUE + "\n\n4.¿En que año se proclamó la independencia del Pérú?" +
          RESET)
    for elementsp4 in lista_p4:
        print(elementsp4)

    respuesta_p4 = input("¿Cúal es tu respuesta?: ")

    while respuesta_p4 not in ("a", "b", "c", "d"):
        respuesta_p4 = input(
            "Debes responder a,b,c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_p4 == "d":
        print(RED +
              "-----------------------------------------------------------" +
              RESET)
        print(
            RED +
            ":v, de verdad estás muy lejos de ser peruano xd. TOTALMENTE INCORRECTO"
            + RESET)
        print(RED +
              "-----------------------------------------------------------" +
              RESET)
        puntaje = puntaje / 2

    elif respuesta_p4 == "a":
        print(
            MAGENTA +
            "--------------------------------------------------------------------------------"
            + RESET)
        print(
            MAGENTA +
            " Uy!! casi, casi; es la respuesta MENOS INDICADA, pero te llevarás unos puntitos"
            + RESET)
        print(
            MAGENTA +
            "--------------------------------------------------------------------------------"
            + RESET)
        puntaje = puntaje + 5

    elif respuesta_p4 == "c":
        print(RED + "--------------------------------------" + RESET)
        print(RED + "Lo siento, es una respuesta INCORRECTA" + RESET)
        print(RED + "--------------------------------------" + RESET)
        puntaje = puntaje - 5

    else:
        print(GREEN + "-----------------------------------------------------" +
              RESET)
        print(GREEN + "CORRECTA!! Muy bien " + nameUser.upper() +
              ", mi parcee!!!|" + RESET)
        print(GREEN +
              "------------------------------------------------------" + RESET)
        puntaje = puntaje * 2

    time.sleep(1)
    print("\t\t\tTu puntaje actual es: ", BLUE + str(puntaje) + RESET)
    time.sleep(1)

    print(BLUE + "\n\n.........................................." + RESET)
    print(BLUE + "Ruleta pa que subas tu puntaje final!! 🥳" + RESET)
    print(BLUE + ".............................................." + RESET)

    listaPuntajeFinal = []
    for a in range(0, 19):
        puntajeFinal = randint(10, 99)
        listaPuntajeFinal.append(puntajeFinal)
        if a == 9:

            print(
                "\n\nSe elegirá un número de aleatorio de la siguiente carita para modificar tu puntaje :D :\n "
            )

        puntajeElegido = choice(listaPuntajeFinal)

    time.sleep(2)
    print(CYAN, "\n\n\t\t\t        ", str(listaPuntajeFinal[10]), "    ",
          str(listaPuntajeFinal[11]))
    time.sleep(2)
    print("\t\t\t        ", str(listaPuntajeFinal[12]), "    ",
          str(listaPuntajeFinal[13]))
    time.sleep(2)
    print("\t\t\t        ", listaPuntajeFinal[14], "    ",
          listaPuntajeFinal[15], RESET)
    time.sleep(2)
    print(WHITE + "\n\n\t\t\t", str(listaPuntajeFinal[0]), "\t\t        ",
          str(listaPuntajeFinal[16]))
    time.sleep(2)
    print("\t\t\t ", str(listaPuntajeFinal[1]), "\t\t       ",
          str(listaPuntajeFinal[9]))
    time.sleep(2)
    print("\t\t\t  ", str(listaPuntajeFinal[2]), "\t\t      ",
          str(listaPuntajeFinal[8]))
    time.sleep(2)
    print("\t\t\t   ", str(listaPuntajeFinal[3]), "\t\t     ",
          str(listaPuntajeFinal[7]))
    time.sleep(2)
    print("\t\t\t    ", str(listaPuntajeFinal[4]), str(listaPuntajeFinal[5]),
          str(listaPuntajeFinal[6]), str(listaPuntajeFinal[16]),
          str(listaPuntajeFinal[17]) + RESET)

    time.sleep(5)
    print(MAGENTA + "\n\n En 3 ... " + RESET)
    time.sleep(4)
    print(GREEN + " 2 ... " + RESET)
    time.sleep(3)
    print(BLUE + " 1 ... " + RESET)
    time.sleep(2)
    print("\nEste es el número elegido de la carita: ",
          BLUE + str(puntajeElegido) + RESET)

    puntajeRuletaFinal = puntajeElegido + puntaje
    time.sleep(1)

    #Mensaje de despedida
    print("\n\nGracias ", BLUE + nameUser.upper() + RESET,
          ", por jugar mi trivia. Obtuviste un total de ... ",
          BLUE + str(puntajeRuletaFinal) + RESET, "puntos.")

    lista_puntaje_por_intentos.append(puntajeRuletaFinal)

    print("\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "\nIngresa 'si' para repetir, o cualquier tecla para finalizar: "
    ).lower()

    if repetir_trivia != "si":
        print(BLUE + "\nTu(s) puntaje(s) en cada ronda de juego fueron: ",
              str(lista_puntaje_por_intentos) + RESET)
        print(f"\nEspero {nameUser} que lo hayas pasado bien, hasta pronto!!!",
              RED + " <3 " + RESET)

        iniciar_trivia = False


"""
#........................................................................................
  #Practicando Condicionales, ej1-------------------------------------



num12 = int(input("Ingrese un número: "))
if num12 >= 0:
 print("El número es positivo")
else:
 print("El número es negativo")

#Practicando Condicionales, ej2-------------------------------------

num = int(input("Ingrese un número: "))

numMultiplicado = num * num

  if numMultiplicado >= 0:
    print("El número es positivo")
  else:
    print("El número es negativo")


#Practicando Condicionales, ej3------------------------------------
num3 = int(input("Ingrese número 1: "))
num4 = int(input("Ingrese número 2: "))

if num3 > num4:
 print("El mayor número es "+ str(num3))

else:
 print("El mayor número es "+ str(num4))

  
#Ejercicio 1-----------------------------------------------------
palabraIntroducida = input("Ingresa una palabra: ")
vecesRepetidas = int(input("Ingresa la cantidad de veces que se repetirá: "))

i = 0
while i < vecesRepetidas:
  print(palabraIntroducida)
  i = i + 1

#Ejercicio 2-----------------------------------------------------
j = 0
while j <= 10:
  if j == 3:
    print("BOOM!")
  else:
    print(j)
  j = j + 1


#Ejercicio 3------------------------------------------------------
filas = int(input("Presione un número para las filas y formar un triángulo: "))
imagen = "+"
k = 0
while k <= filas:
  print(imagen * k) 
  k = k + 1

#-----------------------------------------------------------------



#RETOSS ----------------------------------------------------------
numCalc1 = int(input("Ingrese un número: "))
numCalc2 = int(input("Ingrese otro número: "))
op = input("Ingrese la operación(+, -, *, /): ")

while op not in ("+", "-", "*", "/"):
    op = input(
        "Operador inválido. Debes escribir solo una de las siguientes operaciones (+,-, *, o /): "
    )

if op == "+":
    print("Resultado: ", numCalc1 + numCalc2)
elif op == "-":
    print("Resultado: ", numCalc1 - numCalc2)
elif op == "*":
    print("Resultado: ", numCalc1 * numCalc2)
else:
    print("Resultado: ", numCalc1 / numCalc2)



#Ejercicios Parte2---------------------------------------------
#caso 1
print("\t\t-----Input-----\n")
numProm1 = int(input("Caso 1: ")) + int(input(" "))
#numprom2 = int(input(" "))
resultSuma = numProm1 / 2

#caso 2
numProm2 = int(input("Caso 2: ")) + int(input(" "))
#numprom2 = int(input(" "))
resultSuma2 = numProm2 / 2

#caso 3
numProm3 = int(input("Caso 3: ")) + int(input(" "))
#numprom2 = int(input(" "))
resultSuma3 = numProm3 / 2

print("\n\t\t-----Output-----\n")
print("Caso 1: ", resultSuma)
print("Caso 2: ", resultSuma2)
print("Caso 2: ", resultSuma3)

#Ejercicios Parte2.1---------------------------------------------
#caso 1
print("\n\n\n\t\t\t\t-----OTRO EJERCICIO PERO DE POTENCIA-----\n")
print("\t\t-----Input-----\n")
numElev1 = int(input("Caso 1: "))**int(input(" "))
#numprom2 = int(input(" "))
resultElev1 = numElev1 

#caso 2
numElev2 = int(input("Caso 2: "))**int(input(" "))
#numprom2 = int(input(" "))
resultElev2 = numElev2 

#caso 3
numElev3 = int(input("Caso 3: "))**int(input(" "))
#numprom2 = int(input(" "))
resultElev3 = numElev3 

print("\n\t\t-----Output-----\n")
print("Caso 1: ", resultElev1)
print("Caso 2: ", resultElev2)
print("Caso 2: ", resultElev3)

#Ejercicios Parte2.2---------------------------------------------
#caso 1
print("\n\n\n\t\t\t\t-----OTRO EJERCICIO PERO DE RAIZ CUADRADA-----\n")
print("\t\t-----Input-----\n")
numRaiz1 = int(input("Caso 1: "))
#numprom2 = int(input(" "))
resultRaiz1 = numRaiz1**0.5

#caso 2
numRaiz2 = int(input("Caso 2: "))
#numprom2 = int(input(" "))
resultRaiz2 = numRaiz2**0.5

#caso 3
numRaiz3 = int(input("Caso 3: "))
#numprom2 = int(input(" "))
resultRaiz3 = numRaiz3**0.5

print("\n\t\t-----Output-----\n")
print("Caso 1: ", resultRaiz1)
print("Caso 2: ", resultRaiz2)
print("Caso 2: ", resultRaiz3)

#Ejercicios Parte2.2--------------------------------------------
#caso 1
print(
    "\n\n\n\t\t-----OTRO EJERCICIO PERO DE RAIZ CUADRADA DE LA SUMA DE LOS NÚMEROS-----\n"
)
print("\t\t-----Input-----\n")
numSumSquare1 = int(input("Caso 1: "))**2 + int(input(" "))**2

#numprom2 = int(input(" "))
resultSumSquare1 = (numSumSquare1)**0.5

#caso 2
numSumSquare2 = int(input("Caso 2: "))**2 + int(input(" "))**2

#numprom2 = int(input(" "))
resultSumSquare2 = (numSumSquare2)**0.5

#caso 3
numSumSquare3 = int(input("Caso 3: "))**2 + int(input(" "))**2

#numprom2 = int(input(" "))
resultSumSquare3 = (numSumSquare3)**0.5

print("\n\t\t-----Output-----\n")

print("Caso 2: ", resultSumSquare1)
print("Caso 2: ", resultSumSquare2)
print("Caso 2: ", resultSumSquare3)
"""

#Módulo JUEGO Y COMPARTO
# #Ejercicio 1 -------------------------------------------------------------
# palabra = input("Ingrese la palabra que se repetirá: ")
# numero_veces = int(input(f"Ingrese el número de veces que se repetirá su palabra '{palabra}':  "))

# for a in range(numero_veces):
#   print(palabra)

# #Ejercicio 2 -------------------------------------------------------------
# listaPalabras = []
# for a in range(0,11):
#   listaPalabras.append(a)
# listaPalabras.sort(reverse=True)
# for b in listaPalabras:
#   print(b)

# #Otra manera de hacerlo es así segun silabuz
# for i in range(10,-1,-1):
#   print(i)

# #Ejercicio 3 -------------------------------------------------------------
# filas = int(input("Número de filas pa que se forme el triángulo: "))

# i="+"
# k = 0
# for a in range(k,filas+1):
#   print(a*i)

# #Otra manera de resolver segun silabuz
# filas2 = int(input("Número de filas pa que se forme el triángulo: "))
# for i in range (0, filas2+1):
#   for j in range(0,i):
#     print("+", end= " ")
#   print(" ")

#RETOS Módulo JUEGO Y COMPARTO
# #tu edad
# edad_persona = int(input("Introduce la edad que tienes: "))

# print("Tu has cumplido todos estos años: ")
# for a in range(1, edad_persona+1):
#   print(a)

# #Npumero entero positivo
# numero_positivo = int(input("Escriba un número entero positivo: "))

# for a in range(1,numero_positivo+1, 2):
#   print(a)

# #Factorial
# numero_factorial = int(input("Escriba un número entero para imprimir su factorial: "))
# result = 1
# lista_factorial = []
# for a in range(1, numero_factorial+1, 1):
#   lista_factorial.append(a)

# for x in lista_factorial:
#   result = result * x
#   if x == lista_factorial[-1]:
#     print(result)
