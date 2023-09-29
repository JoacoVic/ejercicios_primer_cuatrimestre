import pygame, sys
from pygame.locals import *
from Colores import *
from Funciones_pygame import *

pygame.init()

PANTALLA = pygame.display.set_mode((500,400))
print(type(PANTALLA))
pygame.display.set_caption("Mi primer ventana.")

PANTALLA.fill(BLANCO)

#pygame.draw.line(PANTALLA,AZUL,(100,100),(350,100),2)
#pygame.draw.rect(PANTALLA,VERDE,(50,50,100,100),2)
#pygame.draw.circle(PANTALLA,ROJO,(250,200),80,40)
# puntos = [(100,300),(100,100),(150,100)]
# pygame.draw.polygon(PANTALLA,OLIVA,puntos,2)

triangulo_rectangulo = mostrar_triangulo_rectangulo_en_ventana(triangulo_rectangulo,PANTALLA)
# circulo = mostrar_circulo_en_ventana(circulo,PANTALLA)
# cuadrado = mostrar_cuadrado_y_rectangulo_en_ventana(cuadrado,PANTALLA)
# rectangulo = mostrar_cuadrado_y_rectangulo_en_ventana(rectangulo,PANTALLA)



flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False
    pygame.display.update()
    
pygame.quit()