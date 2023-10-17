from data_stark import *

#Ejercicio 1
def stark_normalizar_datos(lista):
    """parsea los datos numéricos(altura, peso y fuerza) y verifica que los datos ya no hayan sido parseados anteriormente.

    Args:
        lista (list): la lista con los superheroes.

    Returns:
        bool: retorna True si alguno de los datos fue parseado, y False si no se pudo hacer o ya estaban parseados.
    """
    normalizacion = False
    for dato in lista:
        dato["inteligencia"] = dato["inteligencia"].capitalize()
        if type(dato["altura"]) != float:
            dato["altura"] = float(dato["altura"])
            normalizacion = True
        if type(dato["peso"]) != float:
            dato["peso"] = float(dato["peso"])
            normalizacion = True
        if type(dato["fuerza"]) != int:
            dato["fuerza"] = int(dato["fuerza"])
            normalizacion = True
    return normalizacion

#Ejercicio 1.1

def obtener_dato(diccionario, key):
    """primero valida si el diccionario está vacío, y luego verifica si la clave que se pasa por párametro se encuentra en el diccionario del superheroe.

    Args:
        diccionario (dict): representa a un superheroe de la lista.
        key (str): la clave que se quiere validar.

    Returns:
        bool: retorna True si el dato se encuentra en una de las claves del diccionario, y False si el diccionario está vacío o no encontró la clave.
    """
    if len(diccionario) != 0:
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
def obtener_nombre(diccionario):
    """primero llama a la función 'obtener_dato', y luego busca la clave 'nombre' y devuelve el valor asignado a esa clave.

    Args:
        diccionario (dict): representa al superheroe.

    Returns:
        str|bool: devuelve un mensaje que indica el nombre del superheroe, y si la clave no existe, devuelve un False.
    """
    validacion = obtener_dato(diccionario, "nombre")
    if validacion:
        for dato in diccionario:
            nombre = diccionario["nombre"]
        respuesta = "Nombre: {0}".format(nombre)
    else:
        respuesta = False
    return respuesta

#Ejercicio 2
def obtener_nombre_y_dato(diccionario, key):
    """llama a las funciones 'obtener_dato' y 'obtener_nombre', y devuelve los valores asignados a las claves 'nombre' y la que se ingrese por parámetro.

    Args:
        diccionario (dict): representa al superheroe.
        key (str): es la clave de la que se quiere obtener el valor.

    Returns:
        str|bool: devuelve un mensaje que indica el nombre y el dato del superheroe que se le pasó por parámetro. Si alguna de las claves no existe, devuelve un False.
    """
    dato = obtener_dato(diccionario, key)
    nombre = obtener_nombre(diccionario)
    if nombre and dato:
        dato = diccionario[key]
        respuesta = "{0} | {1}: {2}".format(nombre,key,dato)
    else:
        respuesta = False
    return respuesta

#Ejercicio 3.1
def validar_dato(lista, key):
    """primero valida que la listá no esté vacía, y luego verifica que el valor de la clave que se le pasa por parámetro sea un entero o un flotante.

    Args:
        lista (list): representa la lista de superheroes.
        key (str): es la clave a validar.

    Returns:
        bool: retorna True si el valor de la clave es un entero o un flotante. Caso contrario retorna un False.
    """
    if len(lista) != 0:
        for dato in lista:
            dato_a_evaluar = dato[key]
            if type(dato_a_evaluar) != float and type(dato_a_evaluar) != int:
                validacion = False
            else:
                validacion = True
    else:
        validacion = False
    return validacion
            
def obtener_maximo(lista, key):
    """primero llama a la función 'validar_dato', y luego recorre la lista de superheroes para obtener el máximo valor de la clave que se le pasa por parámetro.

    Args:
        lista (list): la lista de superheroes.
        key (str): la clave de la cual se quiere obtener el máximo.

    Returns:
        int|float|bool: retorna un entero o un flotante (dependiendo del tipo de clave) que representa el valor máximo. En caso de que algún valor no sea un entero o un flotante, retorna un False.
    """
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
def obtener_minimo(lista, key):
    """primero llama a la función 'validar_dato', y luego recorre la lista de superheroes para obtener el mínimo valor de la clave que se le pasa por parámetro.

    Args:
        lista (list): la lista de superheroes.
        key (str): la clave de la cual se quiere obtener el mínimo.

    Returns:
        int|float|bool: retorna un entero o un flotante (dependiendo del tipo de clave) que representa el valor mínimo. En caso de que algún valor no sea un entero o un flotante, retorna un False. 
    """
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
def obtener_dato_cantidad(lista, dato_encontrado, key):
    """recibe un dato que representa el valor del que se quiere encontrar la cantidad y, recorriendo la lista, lo compara con los valores de la misma clave de cada superheroe.
    Args:
        lista (list): la lista de superheroes.
        dato_encontrado (any): es el valor del que se quiere encontrar la cantidad de veces que aparece en la lista.
        key (str): la clave de la cual se obtiene el dato encontrado.

    Returns:
        list: retorna una lista con los superheroes que tengan el mismo dato que el que se quiere encontrar. 
    """
    lista_heroes_encontrados = list()
    for dato in lista:
        if dato[key] == dato_encontrado:
            heroe_encontrado = dato
            lista_heroes_encontrados.append(heroe_encontrado)
    return lista_heroes_encontrados


#Ejercicio 3.4
def stark_imprimir_heroes(lista):
    """imprime por consola todos los datos de la lista que se le pase por parámetro.

    Args:
        lista (list): la lista de superheroes.

    Returns:
        bool|None: retorna False si la lista está vacía. Caso contrario no retorna nada.
    """
    if len(lista) != 0:
        for dato in lista:
            print(f"nombre: {dato['nombre']} - identidad: {dato['identidad']} - empresa: {dato['empresa']} - altura: {dato['altura']:0.2f} - peso: {dato['peso']:0.2f}\ngénero = {dato['genero']} - color de ojos: {dato['color_ojos']} - color de pelo: {dato['color_pelo']} - fuerza: {dato['fuerza']} - inteligencia: {dato['inteligencia']}\n")
    else:
        return False

#Ejercicio 4.1
def sumar_dato_heroe(lista, key):
    """hace un acumulador con todos los valores (enteros o flotantes) de la clave que se le pasa por parámetro.

    Args:
        lista (list): la lista de superheroes.
        key (str): la clave de la cual se obtiene los valores a acumular.

    Returns:
        int|float: retorna el acumulador (en entero o en flotante) que se obtuvo.
    """
    acumulador = 0
    for dato in lista:
        if type(dato) == dict and len(dato) != 0:
            valor = dato[key]
            acumulador += valor
        else:
            acumulador = False
            break
    return acumulador

#Ejercicio 4.2
def dividir(dividendo, divisor):
    """realiza la división entre los valores que se le pasan por parámetro.

    Args:
        dividendo (int|float): lo que se divide.
        divisor (int|float): lo que divide.

    Returns:
        int|float|bool: retorna el resultado de la división (en entero o en flotante). Si el divisor es 0, retorna un False.
    """
    if divisor != 0:
        resultado = dividendo / divisor
    else:
        resultado = False
    return resultado

#Ejercicio 4.3
def calcular_promedio(lista, key):
    """llama a las funciones 'sumar_dato_heroe' y 'dividir' para realizar el promedio de la clave que se pasa por parámetro.

    Args:
        lista (list):la lista de superheroes.
        key (str): la clave de la que se quiere obtener el promedio.

    Returns:
        float: retorna el promedio obtenido.
    """
    acumulador = sumar_dato_heroe(lista, key)
    promedio = dividir(acumulador, len(lista))
    return promedio

#Ejercicio 4.4
def mostrar_promedio_dato(lista, key):
    """llama a la función 'validar_dato' y 'calcular_promedio' para imprimir por consola el promedio obtenido.

    Args:
        lista (list): la lista de superheroes.
        key (str): la clave que requiere las funciones que se llaman dentro. 

    Returns:
        bool|None: si los valores de la clave que se pasa por parámetro no son enteros ni flotantes, retorna un False. Caso contrario no retorna nada.
    """
    dato_a_evaluar = validar_dato(lista, key)
    if dato_a_evaluar:
        promedio = calcular_promedio(lista, key)
        print(f"promedio: {promedio:0.2f}")
    else:
        return False

#Ejercicio 5.1
def imprimir_menu():
    """crea el menú de opciones que tiene el usuario.

    Returns:
        str: retorna el menú. 
    """
    menu = (
    "elija una opcion:\n"
    "1. Normalizar datos\n"
    "2. Nombre de cada superhéroe de género NB\n"
    "3. Superhéroe más alto de género F\n"
    "4. Superhéroe más alto de género M\n"
    "5. Superhéroes más débiles de género M\n"
    "6. Superhéroes más débiles de género NB\n"
    "7. Fuerza promedio de los superhéroes de género NB\n"
    "8. Cuántos superhéroes tienen cada tipo de color de ojos\n"
    "9. Cuántos superhéroes tienen cada tipo de color de pelo\n"
    "10. Listado de todos los superhéroes agrupados por color de ojos\n"
    "11. Listado de todos los superhéroes agrupados por tipo de inteligencia\n"
    "12. Salir\n"
    )
    return menu


#Ejercicio 5.2
def validar_entero(numero):
    """comprueba si el string que se le pasa por parámetro es o son dígito/s.

    Args:
        numero (str): el string que representa un número.

    Returns:
        bool: si el string es o contiene dígito/s, retorna True. Caso contrario retorna False.
    """
    if numero.isdigit():
        validacion = True
    else:
        validacion = False
    return validacion

#Ejercicio 5.3
def stark_menu_principal():
    """llama a la función 'imprimir_menu' y le da al usuario la capacidad de elegir una de las opciones de dicho menú. Luego llama a la función 'validar_entero'.

    Returns:
        int|bool: si el string que ingresa el usuario es o contiene dígito/s retorna ese string. Caso contrario, retorna False. 
    """
    print(imprimir_menu())
    respuesta = input("Elija una opción: ")
    validacion = validar_entero(respuesta)
    if validacion:
        respuesta = int(respuesta)
    else:
        respuesta = False
    return respuesta

#Funciones extra
def obtener_superheroes_por_genero(lista, genero):
    """recibe uno de los géneros que se encuentra en la lista de superheroes, y la recorre para hallar a aquellos que sean del mismo género.

    Args:
        lista (list): la lista de superheroes.
        genero (str): el genero del que se quieren obtener los superheroes.

    Returns:
        list: retorna una lista con los superheroes que sean del mismo género del que se pasa por parámetro.
    """
    lista_genero = list()
    for superheroe in lista:
        genero_encontrado = superheroe["genero"]
        if genero_encontrado == genero:
            lista_genero.append(superheroe)
    return lista_genero

def obtener_datos_string(lista, key):
    """Crea una lista con todos los valores de la key que se le pase por parámetro, y luego con un 'set' elimina todos los repetidos.

    Args:
        lista (list): la lista de superheroes.
        key (str): la clave de la que se quiere obtener los valores.

    Returns:
        list: retorna la lista seteada sin valores repetidos.
    """
    lista_datos = list()
    for heroe in lista:
        dato = heroe[key].capitalize()
        lista_datos.append(dato)
    lista_datos = set(lista_datos)
    return lista_datos

def mostrar_datos_string(lista, key, mensaje):
    """Imprime los valores de la lista que se le pase por parámetro junto con la cantidad de heroes de la lista de personajes que tengan el mismo valor.

    Args:
        lista (list): la lista con los valores específicos.
        key (str): la clave con la que se va a comparar cada valor de la lista pasada por parámetro.
        mensaje (str): un mensaje que sirve para imprimir una respuesta más completa.
    """
    for dato in lista:
        contador = 0
        for heroe in lista_personajes:
            if dato == heroe[key].capitalize():
                contador += 1
        if dato != "":
            print(f"superheroes con {mensaje} {dato}: {contador}")
        else:
            print(f"superheroes sin datos: {contador}")

def mostrar_heroes_por_tipo_de_dato(lista, key, mensaje):
    """Imprime a todos los heroes agrupados con el mismo valor de la clave que se le pasa por parámetro. Llama a las funciones 'obtener_dato_cantidad' y `stark_imprimir_heroes'.

    Args:
        lista (list): la lista con los valores específicos.
        key (str): la clave de la cual se basan los valores específicos.
        mensaje (str): mensaje que sirve para aclarar en la respuesta de a qué valores se refiere.
    """
    for dato in lista:
        lista_por_grupo = obtener_dato_cantidad(lista_personajes,dato,key)
        if dato != "":
            print(f"*Heroes con {mensaje} {dato}:\n")
            stark_imprimir_heroes(lista_por_grupo)
        else:
            print(f"*Heroes sin inteligencia definida:\n")
            stark_imprimir_heroes(lista_por_grupo)
        





#Ejercicio 6
def stark_marvel_app(lista_personajes):
    """Se encarga de todo el funcionamiento del programa, utilizando 'match case' para resolver y mostrar la respuesta de lo que solicita el usuario.

    Args:
        lista_personajes (list): la lista con todos los superheroes.
    """
    bandera = False
    while True:
        opcion = stark_menu_principal()
        if bandera == False:
            if opcion == 1:
                normalizacion = stark_normalizar_datos(lista_personajes)
                if normalizacion:
                    print("Datos normalizados\n")
                    bandera = True
                else:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n")
            else:
                print("No se puede acceder a las otras opciones del menú si los datos no están normalizados\n")
        else:
            match opcion:
                case 1:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n")
    
                case 2:
                    lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
                    for heroe in lista_nb:
                        print(obtener_nombre(heroe))

                case 3:
                    lista_femeninos = obtener_superheroes_por_genero(lista_personajes, "F")
                    maximo_altura = obtener_maximo(lista_femeninos, "altura")
                    lista_respuestas = obtener_dato_cantidad(lista_femeninos,maximo_altura,"altura")
                    stark_imprimir_heroes(lista_respuestas)

                case 4:
                    lista_masculinos = obtener_superheroes_por_genero(lista_personajes, "M")
                    maximo_altura = obtener_maximo(lista_masculinos, "altura")
                    lista_respuestas = obtener_dato_cantidad(lista_masculinos,maximo_altura,"altura")
                    stark_imprimir_heroes(lista_respuestas)

                case 5:
                    lista_masculinos = obtener_superheroes_por_genero(lista_personajes, "M")
                    minimo_fuerza = obtener_minimo(lista_masculinos, "fuerza")
                    lista_respuestas = obtener_dato_cantidad(lista_masculinos,minimo_fuerza,"fuerza")
                    stark_imprimir_heroes(lista_respuestas)
                
                case 6:
                    lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
                    minimo_fuerza = obtener_minimo(lista_nb, "fuerza")
                    lista_respuestas = obtener_dato_cantidad(lista_nb,minimo_fuerza,"fuerza")
                    stark_imprimir_heroes(lista_respuestas)

                case 7:
                    lista_nb = obtener_superheroes_por_genero(lista_personajes, "NB")
                    promedio = calcular_promedio(lista_nb, "fuerza")
                    print(f"promedio de fuerza de los superhéroes no binarios: {promedio:0.2f}\n")

                case 8:
                    lista_colores_ojos = obtener_datos_string(lista_personajes,"color_ojos")
                    mostrar_datos_string(lista_colores_ojos,"color_ojos","ojos")

                case 9:
                    lista_colores_pelo = obtener_datos_string(lista_personajes,"color_pelo")
                    mostrar_datos_string(lista_colores_pelo,"color_pelo","pelo")
                
                case 10:
                    lista_colores_ojos = obtener_datos_string(lista_personajes,"color_ojos")
                    mostrar_heroes_por_tipo_de_dato(lista_colores_ojos, "color_ojos", "ojos")
                
                case 11:
                    lista_inteligencias = obtener_datos_string(lista_personajes,"inteligencia")
                    mostrar_heroes_por_tipo_de_dato(lista_inteligencias,"inteligencia","inteligencia")

                case 12:
                    break

                case _:
                    print("Opción no válida.")

        

stark_marvel_app(lista_personajes)