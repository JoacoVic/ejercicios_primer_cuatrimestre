import math
p = math.pi

#Función 01
def calcular_area_circulo(radio: int):
    area = p * (radio**2)
    return area

#Función 02
def calcular_par_impar(numero: int):
    if numero%2 == 0:
        mensaje = "el numero es par"
    else:
        mensaje = "el numero es impar"
    return mensaje

#Función 03
def sumar_lista_numeros(lista:list):
    acumulador = 0
    for numero in lista:
        acumulador += numero
    return acumulador

#Función 04
def mostrar_numero_maximo(primer_numero, segundo_numero, tercer_numero):
    lista_numeros.append(primer_numero)
    lista_numeros.append(segundo_numero)
    lista_numeros.append(tercer_numero)
    bandera_maximo = False
    for numero in lista_numeros:
        if bandera == False or numero > mayor_numero:
            mayor_numero = numero
            bandera == True
    return mayor_numero

#Función 05
def invertir_cadena(cadena: str):
    largo_cadena = len(cadena)
    cadena_invertida = ""
    for letra in range(len(cadena)):
        largo_cadena -= 1
        cadena_invertida += cadena[largo_cadena]
    return cadena_invertida

#Función 06
def ordenar_lista_alfabeticamente(lista:list):
    return lista.sort()

#Función 07
def calcular_potencia(numero_base:int, numero_potencia:int):
    resultado = numero_base**numero_potencia
    return resultado

#Función 08
def obtener_numeros_pares(lista:list):
    bandera_numeros_pares = False
    lista_numeros_pares = list()
    for numero in lista:
        if numero%2 == 0:
            lista_numeros_pares.append(numero)
            bandera_numeros_pares = True
    if bandera_numeros_pares == True:
        return lista_numeros_pares
    else:
        print("No hay numeros pares en la lista")

#Función 09
def calcular_producto_lista_numeros(lista_numeros: list):
    producto = 1
    for numero in lista_numeros:
        producto *= numero
    
    return producto

#Función 10
def cadenaPalindromo(cadena:str):
    inicio = 0
    fin = len(cadena) -1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False

#Menú opciones
while True:
    respuesta = input("1.Calcular el área de un círculo\n2.Verificar si el numero es par o impar\n3. Sumar una lista de números\n4.Encontrar el máximo de 3 números\n5.Invertir cadena\n6.Ordenar lista de palabras alfabéticamente\n7.Calcular la potencia de un número\n8.Encontrar numeros pares\n9.Calcular el producto de una lista de números\n10.Determinar si la cadena es palíndromo\nSalir\nElija una opción: ")
    while not respuesta.isdigit() or int(respuesta) > 11:
        respuesta = input("Error, intente nuevamente\n1.Calcular el área de un círculo\n2.Verificar si el numero es par o impar\n3. Sumar una lista de números\n4.Encontrar el máximo de 3 números\n5.Invertir cadena\n6.Ordenar lista de palabras alfabéticamente\n7.Calcular la potencia de un número\n8.Encontrar numeros pares\n9.Calcular el producto de una lista de números\n10.Determinar si la cadena es palíndromo\nSalir\nElija una opción: ")
    match respuesta:
        case "1":
            radio = input("Ingrese el radio del círculo: ")
            while not radio.isdigit():
                radio = input("Ingrese el radio del círculo: ")
            radio = int(radio)
            resultado = calcular_area_circulo(radio)
            print(f"El radio del círculo es: {resultado:0.2f}\n")

        case "2":
            numero = input("Ingrese el numero: ")
            while not numero.isdigit():
                numero = input("Ingrese el numero: ")
            numero = int(numero)
            print(calcular_par_impar(numero))

        case "3":
            lista_numeros = list()
            numero = input("Ingrese los numeros a sumar (0 para salir): ")
            while not numero.isdigit():
                numero = input("Error: Ingrese los numeros a sumar (0 para salir): ")
            numero = int(numero)


