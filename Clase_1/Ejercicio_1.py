
'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo
desarrollo en python,
que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
    # Inteligencia artificial (IA),
    # Realidad virtual/aumentada (RV/RA),
    # Internet de las cosas (IOT) o
    # Procesamiento de lenguaje natural (NLP).


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:


A) Los datos a ingresar por cada empleado encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
    50 años inclusive.
    2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
    Femenino o su edad se encuentre entre los 33 y 40.
    3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    de ese género.
'''
import pygame

CELESTE = (0,150,255)
AZUL = (0,0,255)
NEGRO = (0,0,0)

pygame.init()

lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta", "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49, 32, 22, 29, 27, 19, 49, 27, 22, 49, 27]
       
lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Otro", "Femenino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Otro"]
       
lista_tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP", "RV/RA", "RV/RA", "NLP", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]

# for i in range(10):
#     nombre = input("Ingrese el nombre del empleado: ")
#     while nombre != None and not nombre.isalpha():
#         nombre = input("Reingrese el nombre del empleado: ")
#     edad = input("Ingrese la edad del empleado: ")
#     while(edad != None and not edad.isdigit()) or int(edad) < 18:
#         edad = input("Reingrese la edad del empleado (Mayor a 18): ")
#     edad = int(edad)
#     genero = input("Ingrese el genero del empleado: ")
#     while(genero != None and genero.isalpha()) and genero != "Masculino" and genero != "Femenino" and genero != "Otro":
#         genero = input("Reingrese el genero del empleado: ")
#     tecnologia = input("Ingrese la tecnologia del empleado: ")
#     while (tecnologia != None and not tecnologia.isalpha()) and tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT" and tecnologia != "NLP":
#         tecnologia = input("Reingrese la tecnologia del empleado: ")
    
#     lista_nombres.append(nombre)
#     lista_edades.append(edad)
#     lista_generos.append(genero)
#     lista_tecnologias.append(tecnologia)

lista_resultados = []

for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    print(f"{nombre:15} {edad}\t{genero:15}{tecnologia}")

# 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
#     50 años inclusive.
contador = 0
for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]

    if genero == "Masculino":
      if tecnologia == "IOT" or tecnologia == "IA":
        if edad >= 25 and edad <= 50:
            contador += 1

lista_resultados.append(f"Empleados de género masculino que votaron por IOT o IA, cuya edad está entre 25 y 50 años inclusive: {contador}")

# 2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
#     Femenino o su edad se encuentre entre los 33 y 40.
contador_ia = 0
for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]

    if tecnologia != "IA":
        if genero != "Femenino" or (edad >= 33 and edad <= 40):
            contador_ia += 1

porcentaje = (contador_ia * 100) / len(lista_tecnologias)
lista_resultados.append(f"Porcentaje de los que no votaron por IA y su género no es femenino o su edad está entre los 33 y 40: {porcentaje:0.2f}%")

# 3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
#     de ese género.
bandera = False
maximo_edad = 0
lista_empleados = []

for i in range(len(lista_tecnologias)):
    edad = lista_edades[i]
    genero = lista_generos[i]

    if genero == "Masculino":
        if bandera == False or edad > maximo_edad:
            maximo_edad = edad
            bandera == True

for i in range(len(lista_tecnologias)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
        
    if genero == "Masculino" and edad == maximo_edad:
        lista_empleados.append(nombre)
        lista_empleados.append(tecnologia)

lista_resultados.append(f"\tNombre y tecnología de los de género masculino con la mayor edad: {lista_empleados}")

fuente = pygame.font.SysFont("Arial", 10)

VENTANA = pygame.display.set_mode((1300,500)) #Pixeles (500->width, 500->height)
pygame.display.set_caption("Mostrar resultados en la ventana")
VENTANA.fill(CELESTE)

fuente = pygame.font.SysFont("Arial", 30)

flag = True
while flag == True:
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    pygame.display.update()

    for resultado in lista_resultados:
        texto = fuente.render(resultado,False,AZUL,NEGRO)
        VENTANA.blit(texto,(50,y))
        y += 35
    
    pygame.display.update()

pygame.quit()
