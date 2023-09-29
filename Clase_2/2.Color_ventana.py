import pygame

BLANCO = (255,255,255)
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
CELESTE = (0,150,255)
NEGRO = (0,0,0)



pygame.init()

VENTANA = pygame.display.set_mode((500,500)) #Pixeles (500->width, 500->height)
pygame.display.set_caption("Mi primer ventana en pygame")
VENTANA.fill(AZUL)



flag = True
while flag == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

    pygame.display.update()

pygame.quit()