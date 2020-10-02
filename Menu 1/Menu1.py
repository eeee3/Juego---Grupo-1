import pygame

largo_pantalla=600

alto_pantalla=600

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    
    def update(self):
        self.left, self.top = pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):

    def __init__(self,imagen1,imagen2,x,y):

        self.imagen=imagen1
        self.imagen2=imagen2
        self.imagenactual=imagen1
        self.rect=self.imagenactual.get_rect()
        self.rect.left, self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):

        if cursor.colliderect(self.rect):
            self.imagenactual=self.imagen2
        else:
            self.imagenactual=self.imagen
        
        pantalla.blit(self.imagenactual, self.rect)

def main():

    hecho = True

    pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

    pygame.display.set_caption("Menu 1")

    reloj1=pygame.time.Clock()

    play=pygame.image.load("play.jpeg")

    play1=pygame.image.load("play1.jpeg")

    quit1=pygame.image.load("quit.jpeg")

    quit2=pygame.image.load("quit1.jpeg")

    boton1=Boton(play,play1,200,300)

    boton2=Boton(quit1,quit2,200,450)

    cursor1=Cursor()

    BLANCO=(255,255,255)

    ROJO=(200,0,0)

    AZUL=(0,0,200)

    colordefondo=BLANCO

    while hecho:

        for evento in pygame.event.get(): 
            if evento.type == pygame.QUIT:
                hecho = False
            if evento.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    colordefondo=ROJO
                if cursor1.colliderect(boton2.rect):
                    colordefondo=AZUL

        reloj1.tick(30)

        pantalla.fill(colordefondo)

        cursor1.update()

        boton1.update(pantalla, cursor1)

        boton2.update(pantalla, cursor1)

        pygame.display.update()

    pygame.quit() 

main()