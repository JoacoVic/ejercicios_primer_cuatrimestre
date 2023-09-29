#PROMEDIO VIDEO 
def calcular_promedio(lista):
    acumulador = 0
    for video in lista:
        duracion = video["length"]
        acumulador += duracion

    promedio = acumulador / len(lista)

    return promedio
#REOCOMENDACION: SI HAY MAS DE UN FOR ES PORQUE PROBABLMENTE EL LOGARITMO SE PUEDE REDUCIR EN FUNCIONES
#######################################################################

def buscar_temas_maximos_key(lista:list,key:str, mensaje:str):
    maximo = buscar_maximo_key(lista,key)
    print (f"{mensaje}:{maximo}")
    mostrar_titulos_maximos(lista,maximo,key)

###### Busca el maximo por clave/key 
def buscar_maximo_key(lista:list, key:str):
    bandera_primero = False
    for video in lista:
        valor = video[key]
        if bandera_primero == False or valor > maximo:
            maximo = valor
            bandera_primero = True
    return maximo

##### Muestra los titulos 

def mostrar_titulos_maximos(lista:list, maximo_vistas:int, key:str):
    for video in lista:
        valor = video[key]
        titulo = video["title"]
        if valor == maximo_vistas:
            print (f"\n{titulo}")
