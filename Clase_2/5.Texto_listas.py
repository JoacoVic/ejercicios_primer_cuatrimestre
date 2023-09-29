import pygame

BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)

lista_animales = ["Perro de las praderas", "Perro", "Gato", "Pajarito", "Cocodrilo"]


pygame.init()

VENTANA = pygame.display.set_mode((900,500)) #Pixeles (500->width, 500->height)
pygame.display.set_caption("Mi primer ventana en pygame")

icono = pygame.image.load("utn_icono.jpg")
pygame.display.set_icon(icono)
VENTANA.fill(AZUL)

fuente = pygame.font.SysFont("Arial", 30)

flag = True
while flag == True:
    y = 50
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    for animal in lista_animales:
        texto = fuente.render(animal,False,ROJO,VERDE)
        VENTANA.blit(texto,(50,y))
        y += 35
    pygame.display.update()


pygame.quit()