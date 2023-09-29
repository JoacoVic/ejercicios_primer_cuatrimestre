AGUA = ( 0, 255, 255)
NEGRO = (0, 0, 0)
AZUL = ( 0, 0, 255)
FUCCIA = (255, 0, 255)
GRIS = (128, 128, 128)
VERDE = (0,128,0)
LIMA = ( 0,255, 0)
MARRON = (128, 0, 0)
AZUL_MARINO = ( 0, 0,128)
OLIVA = (128, 128, 0)
PURPURA = (128, 0, 128)
ROJO = (255, 0, 0)
PLATEADO = (192, 192, 192)
BLANCO = (255, 255, 255)
YELLOW = (255, 255, 0)

import pygame, sys
from pygame.locals import *

pygame.init()#Para inicializar pygame

ventana = pygame.display.set_mode((1300,700)) # en pixeles (width=Largo, height=Alto)
pygame.display.set_caption("Datos de mis mascotas")#Titulo de la ventana

ventana.fill(FUCCIA)
fuente = pygame.font.SysFont("Arial", 30)


animal_uno = {"nombre": "puppy", "edad": "2", "imagen": "Clase_4\perrito.jpg"}
animal_dos = {"nombre": "kitty", "edad": "3", "imagen": "Clase_4\gatito.jpg"}
animal_tres = {"nombre": "bunny", "edad": "4", "imagen": "Clase_4\conejito.jpg"}

lista_animales = [animal_uno, animal_dos, animal_tres]

flag_run = True
while flag_run:#Bucle infinito. Todo lo que necesitamos que se repita de manera indeterminada...
    #Las siguientes lineas permiten capturar eventos. Por ejemplo si el usuario presiona alguna tecla especifica.
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:#Preguntamos si presionó X. (Esto es el evento QUIT de pygame)
            flag_run = False
    for animal in lista_animales:
        nombre = animal["nombre"]
        edad = animal["edad"]
        imagen = animal["imagen"]

        animal_imagen = pygame.image.load(imagen)
        animal_imagen = pygame.transform.scale(animal_imagen,(200,100))


        texto_uno = fuente.render(nombre,False,NEGRO,PLATEADO)
        texto_dos = fuente.render(edad,False,NEGRO,PLATEADO)

        ventana.blit(texto_uno, (100,y))
        ventana.blit(texto_dos, (500,y))
        ventana.blit(animal_imagen, (700,y))

        y += 235




    pygame.display.update()
    
pygame.quit()