import pygame, sys
from pygame.locals import *

pygame.init()#Para inicializar pygame

ventana = pygame.display.set_mode((900,500)) # en pixeles (width=Largo, height=Alto)
pygame.display.set_caption("Mi primer ventana.")#Titulo de la ventana

imagen = pygame.image.load("Clase_4\imagen_3.jpg")
imagen = pygame.transform.scale(imagen, (200,200))

otra_imagen = pygame.image.load("Clase_4\imagen_2.jpg")
otra_imagen = pygame.transform.scale(otra_imagen, (200,200))
otra_imagen = pygame.transform.flip(otra_imagen,True,False)

flag_run = True
while flag_run:#Bucle infinito. Todo lo que necesitamos que se repita de manera indeterminada...
    #Las siguientes lineas permiten capturar eventos. Por ejemplo si el usuario presiona alguna tecla especifica.
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:#Preguntamos si presionó X. (Esto es el evento QUIT de pygame)
            flag_run = False
    ventana.blit(imagen, (50, 50))
    ventana.blit(otra_imagen, (150, 50))
    pygame.display.update()
    
pygame.quit()