import re
from data_stark import *

#Ejercicio 1.1
def extraer_iniciales(nombre_heroe):
    """analiza el nombre que se le pasa por parámetro y lo devuelve con solamente las iniciales separadas por un punto. También reemplaza los guiones por espacios en blanco y elimina la palabra 'the'.

    Args:
        nombre_heroe (str): el nombre que se quiere modificar.

    Returns:
        str: las iniciales del nombre separadas por un punto. si el dato pasado por parámetro es un string vacío, devuelve 'N/A'.
    """
    if nombre_heroe != "":
        sin_guion = re.sub("-"," ",nombre_heroe)
        sin_the = re.sub(" the ","",sin_guion)
        iniciales = re.sub("[a-z ]+",".",sin_the)
    else:
        iniciales = "N/A"
    return iniciales

#Ejercicio 1.2
def obtener_dato_formato(dato):
    """convierte todo el dato a minúsculas, con las palabras separadas por un guión bajo.

    Args:
        dato (str): el dato que se modifica.

    Returns:
        str|bool: retorna el string modificado si todo salió bien, o un False si el dato no es un string.
    """
    if type(dato) == str:
        mayusculas = re.findall("[A-Z]+",dato)
        for letra in mayusculas:
            minusculas = re.sub(letra, letra.lower(), dato)
            dato = minusculas
        formato = re.sub(" ","_",dato)
    else:
        formato = False
    return formato

#Ejercicio 1.3
def stark_imprimir_nombre_con_iniciales(heroe):
    """llama a las funciones 'extraer_iniciales' y 'obtener_dato_formato' para luego unir ambos strings.

    Args:
        heroe (dict): el heroe del que se obtiene el nombre.

    Returns:
        bool|str: retorna la unión si todo salió bien. Caso contrario retorna False.
    """
    resultado = False
    if type(heroe) == dict:
        for clave in heroe:
            if clave == "nombre":
                iniciales = extraer_iniciales(heroe[clave])
                nombre_formateado = obtener_dato_formato(heroe[clave])
                union_datos = "".join(["*",nombre_formateado,f" ({iniciales})"])
                resultado = union_datos #Retorno el resultado en vez de True porque sino no la puedo reutilizar en los siguientes llamados en donde la necesito y tendría que repetir código.
                break
    return resultado

#Ejercicio 1.4
def stark_imprimir_nombres_con_iniciales(lista):
    """llama a la función 'stark_imprimir_nombre_con_iniciales' para que imprima los nombres modificados de todos los heroes de la lista.

    Args:
        lista (list): la lista de personajes.

    Returns:
        bool|None: si la lista está vacía o el dato que se le pasa por parámetro no es del tipo lista, la función devuelve un False. Caso contrario no retorna nada.
    """
    if len(lista) != 0 and type(lista) == list:
        for heroe in lista:
            print(stark_imprimir_nombre_con_iniciales(heroe))
        resultado = True
    else:
        resultado = False
    return resultado

#Ejercicio 2.1
def generar_codigo_heroe(heroe,id_heroe):
    """crea el código del héroe uniendo los siguientes datos: el género, un guión, el primer numero del código dependiendo del género, el id del heroe al final y los ceros necesarios para que el código tenga 10 caracteres.

    Args:
        heroe (dict): el heroe del que se quiere obtener el código.
        id_heroe (int): la posición que ocupa en la lista.

    Returns:
        str: retorna el código completo si todo salió bien, sino retorna 'N/A'.
    """
    genero = heroe["genero"]
    id_heroe = str(id_heroe)
    match genero:
        case "F":
            inicio_genero = "2"
        case "M":
            inicio_genero = "1"
        case "NB":
            inicio_genero = "0"
        case _:
            inicio_genero = "N/A"
    if inicio_genero != "N/A":
        union_datos = "".join([genero,"-",inicio_genero])
        ceros_necesarios = id_heroe.zfill(10-len(union_datos))
        dato_completo = "".join([union_datos, ceros_necesarios])
    else:
        dato_completo = "N/A"
    return dato_completo

#Ejercicio 2.2
def stark_generar_codigo_heroe(lista):
    """crea una cadena con todos los nombres de los heroes modificados y su código correspondiente llamando a las funciones 'generar_codigo_heroe' y 'stark_imprimir_nombre_con_iniciales'.

    Args:
        lista (list): la lista de personajes

    Returns:
        str: la cadena generada con todos los nombres modificados y los códigos.
    """
    contador_indice = 1
    bandera = False
    for heroe in lista_personajes:
        dato_genero = generar_codigo_heroe(heroe, contador_indice)
        nombre = stark_imprimir_nombre_con_iniciales(heroe)
        respuesta_actual = " | ".join([nombre,dato_genero])
        if bandera == False:
            respuesta_final = respuesta_actual
            bandera = True
        else:
            respuesta_anterior = respuesta_final
            respuesta_final = "\n".join([respuesta_anterior, respuesta_actual])
        contador_indice += 1
    respuesta_final = "\n".join([respuesta_final,f"Se asignaron {contador_indice-1} códigos"])
    return respuesta_final

#Ejercicio 3.1
def sanitizar_entero(numero):
    """realiza un .strip() al string y luego lo parsea a entero, validando con try except los posibles errores durante la conversión.

    Args:
        numero (str): el numero que se quiere sanitizar.

    Returns:
        int: dependiendo del tipo de error, devuelve valores del -1 hasta el -3. Si la sanitización se logra correctamente, retorna el numero parseado.
    """
    try:
        numero = numero.strip()
        numero = int(numero)
        if numero < 0:
            resultado = -2
        else:
            resultado = numero
    except ValueError:
        resultado = -1
    except:
        resultado = -3
    return resultado

#Ejercicio 3.2
def sanitizar_flotante(numero):
    """realiza un .strip() al string y luego lo parsea a flotante, validando con try except los posibles errores durante la conversión.

    Args:
        numero (str): el numero que se quiere parsear.

    Returns:
        int|float: dependiendo del tipo de error, devuelve valores del -1 hasta el -3. Si la sanitización se logra correctamente, retorna el numero flotante.
    """
    try:
        numero = numero.strip()
        numero = float(numero)
        if numero < 0:
            resultado = -2
        else:
            resultado = round(numero,2)
    except ValueError:
        resultado = -1
    except:
        resultado = -3
    return resultado

#Ejercicio 3.3
def sanitizar_string(valor, valor_por_defecto="-"):
    """realiza un .strip() al string y luego verifica que el string no contenga números; si encuentra una barra, la reemplaza con un espacio en blanco.

    Args:
        valor (str): el string que se quiere sanitizar.
        valor_por_defecto (str, optional): se utiliza si el valor inicial es un string vacío. Defaults to "-".

    Returns:
        str: retorna el string sin numeros, sin barras y en minusculas.
    """
    resultado = False
    if (valor == "" and valor_por_defecto != "-"):
        valor = valor_por_defecto
    valor = valor.strip()
    if re.search("[0-9]",valor) != None:
        resultado = "N/A"
    elif re.search("/",valor) != None:
        valor = re.sub("/"," ",valor)
        resultado = valor.lower()
    else:
        resultado = valor.lower()
    return resultado

#Ejercicio 3.4
def sanitizar_dato(heroe, clave, tipo_dato):
    """reutiliza las funciones que empiezan el 'sanitizar', dependiendo del tipo de dato. Si la sanitización se hace correctamente, modifica el valor del heroe con el dato sanitizado.

    Args:
        heroe (dict): el heroe que se quiere sanitizar.
        clave (str): la clave con el valor que se quiere sanitizar.
        tipo_dato (str): tiene que ser un entero, un flotante o un string.

    Returns:
        bool: si alguna de las sanitizaciones se efectúa, retorna True. Caso contrario retorna False.
    """
    resultado = False
    clave = clave.lower()
    tipo_dato = tipo_dato.lower()
    dato_a_sanitizar = heroe[clave]
    for dato in heroe:
        if clave == dato:
            if tipo_dato == "entero":
                dato_sanitizado = sanitizar_entero(dato_a_sanitizar)
                if dato_sanitizado > 0:
                    heroe[clave] = dato_sanitizado
                    resultado = True
            elif tipo_dato == "flotante":
                dato_sanitizado = sanitizar_flotante(dato_a_sanitizar)
                if dato_sanitizado > 0:
                    heroe[clave] = dato_sanitizado
                    resultado = True
            elif tipo_dato == "string":
                dato_sanitizado = sanitizar_string(dato_a_sanitizar,"No tiene")
                if dato_sanitizado != "N/A":
                    heroe[clave] = dato_sanitizado
                    resultado = True
            else:
                print("Tipo de dato no reconocido")
            break
    return resultado

#Ejercicio 3.5
def stark_normalizar_datos(lista):
    """normaliza los datos de 'altura', 'peso', 'fuerza', 'color_ojos', 'color_pelo' e 'inteligencia' llamando a la función 'sanitizar_dato'.

    Args:
        lista (list): la lista de personajes.

    Returns:
        bool: si alguna sanitización se cumplió, retorna True. Caso contrario retorna False.
    """
    normalizacion = False
    if len(lista) != 0:
        for dato in lista:
            conversion_altura = sanitizar_dato(dato,"altura","flotante")
            if conversion_altura:
                normalizacion = True

            conversion_peso = sanitizar_dato(dato,"peso","flotante")
            if conversion_peso:
                normalizacion = True

            conversion_fuerza = sanitizar_dato(dato,"fuerza","entero")
            if conversion_fuerza:
                normalizacion = True

            conversion_ojos = sanitizar_dato(dato,"color_ojos","string")

            conversion_pelo = sanitizar_dato(dato,"color_pelo","string")

            conversion_inteligencia = sanitizar_dato(dato,"inteligencia","string")
    else:
        print("Error: lista de héroes vacía")
    return normalizacion

#Ejercicio 4.1
def stark_imprimir_indice_nombre(lista):
    """une todos los nombres de los superheroes con snake_case en un string y lo imprime. Llama a la función 'obtener_dato_formato' para facilitar el proceso.

    Args:
        lista (list): la lista de personajes
    """
    bandera = False
    for heroe in lista:
        formato = obtener_dato_formato(heroe["nombre"])
        if re.search("the",formato) != None:
            nombre_sin_the = re.sub("the","",formato)
            nombre_actual = re.sub(r"_+","-",nombre_sin_the)
        else:
            nombre_actual = re.sub(r"_+","-",formato)

        if bandera == False:
            union_nombres = nombre_actual
            bandera = True
        else:
            nombre_anterior = union_nombres
            union_nombres = "-".join([nombre_anterior,nombre_actual])
    print(union_nombres)

#Ejercicio 5.1
def generar_separador(patron, largo, imprimir=True):
    """crea un separador (con un patrón que se le pasa por parámetro) con un largo determinado en otro parámetro. Por defecto lo imprime pero puede solo devolverlo.  

    Args:
        patron (str): lo que se va a usar como separador.
        largo (int): cuantas veces se va a generar el separador.
        imprimir (bool, optional): por defecto imprime el separador. Si se le pasa False, lo retorna. Defaults to True.

    Returns:
        str: Si se pide, retorna el separador si todo salió bien, o 'N/A' en caso contrario.
    """
    bandera = False
    retorno = ""
    if type(patron) == str and (len(patron) == 1 or len(patron) == 2):
        if type(largo) == int and (largo >= 1 and largo <= 235):
            for caracter in range(largo):
                caracter = patron
                if bandera == False:
                    union_caracteres = caracter
                    bandera = True
                else:
                    caracter_anterior = union_caracteres
                    union_caracteres = "".join([caracter_anterior,caracter])
            if imprimir:
                print(union_caracteres)
            else:
                retorno = union_caracteres
        else:
            retorno = "N/A"
    else:
        retorno = "N/A"
    return retorno

#Ejercicio 5.2
def generar_encabezado(titulo):
    """llama a la función 'generar_separador', y con el título que se le pasa por parámetro, crea el encabezado.

    Args:
        titulo (str): el título que va a estar en el encabezado.

    Returns:
        str: retorna el formato del encabezado.
    """
    primer_linea_separador = generar_separador("*",146,False)
    titulo_encabezado = titulo.upper()
    segunda_linea_separador = generar_separador("*",146,False)
    union = "\n".join([primer_linea_separador,titulo_encabezado,segunda_linea_separador])
    return union
    
#Ejercicio 5.3
def imprimir_ficha_heroe(heroe):
    """crea la ficha del heroe que se le pasa por parámetro con todos sus datos organizados con sus encabezados respectivos. Llama a las funciones 'generar_encabezado', 'stark_imprimir_nombre_con_iniciales' y 'obtener_dato_formato' cuando lo necesita.

    Args:
        heroe (dict): el superheroe del que se va a crear la ficha.

    Returns:
        str: un string con la ficha completa del superheroe.
    """
    encabezado_principal = generar_encabezado("principal")
    nombre = "\t".join(["NOMBRE DEL HÉROE:",stark_imprimir_nombre_con_iniciales(heroe)])
    nombre_corregido = re.sub(r"\*","",nombre)
    identidad = "\t".join(["IDENTIDAD SECRETA:",obtener_dato_formato(heroe["identidad"])])
    empresa = "\t\t".join(["CONSULTORA:",obtener_dato_formato(heroe["empresa"])])
    codigo = "\t".join(["CÓDIGO DEL HÉROE:",generar_codigo_heroe(heroe,(lista_personajes.index(heroe)+1))])
    encabezado_fisico = generar_encabezado("físico")
    altura = "\t\t\t".join(["ALTURA:",f"{heroe['altura']} cm."])
    peso = "\t\t\t".join(["PESO:",f"{heroe['peso']} kg."])
    fuerza = "\t\t\t".join(["FUERZA:",f"{heroe['fuerza']} N."])
    encabezado_particular = generar_encabezado("señas particulares")
    color_ojos = "\t\t".join(["COLOR DE OJOS:",heroe["color_ojos"].capitalize()])
    color_pelo = "\t\t".join(["COLOR DE PELO:",heroe["color_pelo"].capitalize()])

    todos_los_datos = "\n".join([encabezado_principal,nombre_corregido,identidad,empresa,codigo,encabezado_fisico,altura,peso,fuerza,encabezado_particular,color_ojos,color_pelo])
    return todos_los_datos

#Ejercicio 5.4

def stark_navegar_fichas(lista:list):
    """llama a la función 'imprimir_ficha_heroe' y le permite al usuario interactuar con todas las fichas de superheroes de la lista, yendo a la anterior o a la siguiente.

    Args:
        lista (list): la lista de superheroes.
    """
    bandera = False
    for heroe in lista_personajes:
        if bandera == False:
            primer_heroe = print(imprimir_ficha_heroe(lista_personajes[0]))
            heroe_actual = heroe
            bandera = True
        posicion_heroe_actual = lista_personajes.index(heroe_actual)
        posicion_heroe_anterior = lista_personajes.index(heroe_actual)-1
        posicion_heroe_siguiente = lista_personajes.index(heroe_actual)+1
        opcion = input(
            "[1] Ir a la izquierda.\n"
            "[2] Ir a la derecha.\n"
            "[3] Volver al menú principal.\n"
            "Seleccione una opción: ")
        match opcion:
            case "1":
                print(imprimir_ficha_heroe(lista_personajes[posicion_heroe_anterior]))
                heroe_actual = lista_personajes[posicion_heroe_anterior]
            case "2":
                try:
                    print(imprimir_ficha_heroe(lista_personajes[posicion_heroe_siguiente]))
                    heroe_actual = lista_personajes[posicion_heroe_siguiente]
                except IndexError:
                    print(imprimir_ficha_heroe(lista_personajes[0]))
                    heroe_actual = lista_personajes[0]
            case "3":
                break
            case _:
                print(opcion)

def stark_marvel_app(lista:list):
    """se encarga del funcionamiento del código. Le muestra al usuario un menú de opciones, y con un match case imprime lo que solicita el usuario.

    Args:
        lista (list): la lista de personajes para que inicie la función.
    """
    while True:
        print("1. Imprimir la lista de nombres junto con sus iniciales.\n"
        "2. Imprimir la lista de nombres y el código del mismo.\n"
        "3. Normalizar datos.\n"
        "4. Imprimir índice de nombres.\n"
        "5. Navegar fichas (Se recomienda sanitizar datos previamente a esta opción).\n"
        "6. Salir.")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                stark_imprimir_nombres_con_iniciales(lista)

            case "2":
                print(stark_generar_codigo_heroe(lista))

            case "3":
                validacion = stark_normalizar_datos(lista)
                if validacion:
                    print("Datos normalizados.\n")
                else:
                    print("Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente\n")
                
            case "4":
                stark_imprimir_indice_nombre(lista)

            case "5":
                stark_navegar_fichas(lista)

            case "6":
                break
            case _:
                print("Error: opción no válida")

stark_marvel_app(lista_personajes)