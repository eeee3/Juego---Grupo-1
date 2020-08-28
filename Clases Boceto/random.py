import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Tutorial Siete")

Mi_imagen = pygame.image.load("Descargas/main-1.png")
posX = randint(10, 300)
posY = randint(10, 200)

print posX, posY
ventana.blit(Mi_imagen, (posX, posY))
whilte True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()








