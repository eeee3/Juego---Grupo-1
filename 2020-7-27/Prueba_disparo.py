import pygame

ROJO = (255, 0, 0)

BLANCO = (255, 255, 255)

class Personaje(pygame.sprite.Sprite):

    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = largo_pantalla/2
        self.rect.y = alto_pantalla/2
        self.listaDisparo= []

    def mover_izq(self):
        self.rect.x-=10
    def mover_der(self):
        self.rect.x+=10
    def mover_arriba(self):
        self.rect.y-=10
    def mover_abajo(self):
        self.rect.y+=10 

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil = pygame.image.load("disparo.png")

        self.rect = self. imageProyectil.get_rect()

        self.velocidadDisparo = 5

        self.rect.top = posy

        self.rect.left = posx

    def trayectoria(self):

        self.rect.top = self.rect.top - self.velocidadDisparo

    def dibujar(self, superficie):

        superficie.blit(self.imageProyectil, self.rect)

    
pygame.init()

largo_pantalla = 700
alto_pantalla = 400
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

bloque_lista = pygame.sprite.Group()

listade_todoslos_sprites= pygame.sprite.Group()

protagonista = Personaje(ROJO, 20, 15)

proyectil1 = Proyectil(largo_pantalla/2, alto_pantalla/2)

listade_todoslos_sprites.add(protagonista)

hecho = False

reloj = pygame.time.Clock()
  
puntuacion = 0

while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                protagonista.mover_izq()
            if evento.key == pygame.K_RIGHT:
                protagonista.mover_der()
            if evento.key == pygame.K_UP:
                protagonista.mover_arriba()
            if evento.key == pygame.K_DOWN:
                protagonista.mover_abajo()
            
    pantalla.fill(BLANCO)

    proyectil1.trayectoria()

    proyectil1.dibujar(pantalla)

    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)

    listade_todoslos_sprites.draw(pantalla)
      
    reloj.tick(60)

    pygame.display.flip()
  
pygame.quit()