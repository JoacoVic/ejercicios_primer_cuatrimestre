from data_stark import lista_personajes
diccionario_superheroe =\
    {
    "nombre": "Thing",
    "identidad": "Ben Grimm",
    "empresa": "Marvel Comics",
    "altura": "183.55000000000001",
    "peso": "225.41999999999999",
    "genero": "M",
    "color_ojos": "Blue",
    "color_pelo": "No Hair",
    "fuerza": "85",
    "inteligencia": "good"
  }

#Ejercicio 1
def stark_normalizar_datos(lista:list)->bool:
    normalizacion = False
    for dato in lista:
        altura = dato["altura"]
        peso = dato["peso"]
        fuerza = dato["fuerza"]
        if type(altura) != float:
            dato["altura"] = float(altura)
            normalizacion = True
        if type(peso) != float:
            dato["peso"] = float(peso)
            normalizacion = True
        if type(fuerza) != int:
            dato["fuerza"] = int(fuerza)
            normalizacion = True
    return normalizacion

#Ejercicio 1.1
def validar_diccionario_vacio(diccionario:dict)->bool:
    if len(diccionario) == 0:
        validacion = False
    else:
        validacion = True

    return validacion

def obtener_dato(diccionario:dict, key:str)->bool:
    validacion_diccionario = validar_diccionario_vacio(diccionario)
    if validacion_diccionario:
        for clave in diccionario:
            if key == clave:
                validacion = True
                break
            else:
                validacion = False
    else:
        validacion = False

    return validacion

#Ejercicio 1.2
def obtener_nombre(diccionario:dict)->str or bool:
    validacion = obtener_dato(diccionario, "nombre")
    if validacion:
        for dato in diccionario:
            nombre = diccionario["nombre"]
        respuesta = "Nombre: {0}".format(nombre)
    else:
        respuesta = False
    return respuesta
print(obtener_nombre(diccionario_superheroe))

#Ejercicio 2
def obtener_nombre_y_dato(diccionario:dict, key:str)->str or bool:
    dato = obtener_dato(diccionario, key)
    nombre = obtener_nombre(diccionario)
    if nombre and dato:
        dato = diccionario[key]
        respuesta = "{0} | {1}: {2}".format(nombre,key,dato)
    else:
        respuesta = False
    return respuesta

#Ejercicio 3.1
def validar_lista_vacia(lista:list):
    if len(lista) == 0:
        estado_lista = False
    else:
        estado_lista = True
    return estado_lista

def validar_dato(lista:list, key:str)->bool:
    estado_lista = validar_lista_vacia(lista)
    if estado_lista:
        for dato in lista:
            dato_a_evaluar = dato[key]
            if type(dato_a_evaluar) != float and type(dato_a_evaluar) != int:
                validacion = False
            else:
                validacion = True
    else:
        validacion = False
    return validacion
            
def obtener_maximo(lista:list, key:str)->int or float or bool:
    validacion = validar_dato(lista, key)
    if validacion:
        bandera = False
        for dato in lista:
            valor = dato[key]
            if bandera == False or valor > maximo:
                maximo = valor
                bandera = True
    else:
        maximo = False
    return maximo

#Ejercicio 3.2
def obtener_minimo(lista:list, key:str)->int or float or bool:
    validacion = validar_dato(lista, key)
    if validacion:
        bandera = False
        for dato in lista:
            valor = dato[key]
            if bandera == False or valor < minimo:
                minimo = valor
                bandera = True
    else:
        minimo = False
    return minimo

#Ejercicio 3.3
def obtener_dato_cantidad(lista:list, dato_encontrado: int, key: str)->list or bool:
    lista_heroes_encontrados = list()
    for dato in lista:
        dato_a_evaluar = dato[key]
        if dato_a_evaluar == dato_encontrado:
            heroe_encontrado = dato
            lista_heroes_encontrados.append(heroe_encontrado)
    return lista_heroes_encontrados


#Ejercicio 3.4
def stark_imprimir_heroes(lista:list):
    estado_lista = validar_lista_vacia(lista)
    if estado_lista:
        for dato in lista:
            nombre = dato["nombre"]
            identidad = dato["identidad"]
            empresa = dato["empresa"]
            altura = dato["altura"]
            peso = dato["peso"]
            genero = dato["genero"]
            color_ojos = dato["color_ojos"]
            color_pelo = dato["color_pelo"]
            fuerza = dato["fuerza"]
            inteligencia = dato["inteligencia"]
            print(f"nombre: {nombre} - identidad: {identidad} - empresa: {empresa} - altura: {altura:0.2f} - peso: {peso:0.2f}\ngénero = {genero} - color de ojos: {color_ojos} - color de pelo: {color_pelo} - fuerza: {fuerza} - inteligencia: {inteligencia}\n")

#Ejercicio 4.1
def obtener_dato_numerico_key(diccionario: dict, key:str):
    for dato in diccionario:
        valor = diccionario[key]
        break
    return valor

def sumar_dato_heroe(lista:list, key:str):
    acumulador = 0
    for dato in lista:
        valor = obtener_dato_numerico_key(dato, key)
        acumulador += valor
    return acumulador

#Ejercicio 4.2
def dividir(dividendo:int or float, divisor:int or float)->int or float or bool:
    if divisor != 0:
        resultado = dividendo / divisor
    else:
        resultado = False
    return resultado

#Ejercicio 4.3
def calcular_promedio(lista: list, key: str)->bool:
    acumulador = sumar_dato_heroe(lista, key)
    promedio = dividir(acumulador, len(lista))
    return promedio

#Ejercicio 4.4
def mostrar_promedio_dato(lista:list, key:str)->bool or None:
    dato_a_evaluar = validar_dato(lista, key)
    if dato_a_evaluar:
        promedio = calcular_promedio(lista, key)
        print(f"promedio: {promedio:0.2f}")
    else:
        return False

#Ejercicio 5.1



#Ejercicio 5.2
def validar_entero(numero:str)->bool:
    if numero.isdigit():
        validacion = True
    else:
        validacion = False
    return validacion