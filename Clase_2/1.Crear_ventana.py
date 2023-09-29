import pygame

pygame.init()

pygame.display.set_mode((500,500)) #Pixeles (500->width, 500->height)
pygame.display.set_caption("Mi primer ventana en pygame")

flag = True
while flag == True:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False

pygame.quit()