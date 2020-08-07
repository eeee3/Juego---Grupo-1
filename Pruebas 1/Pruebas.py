import pygame
import random
ROJO = (255, 0, 0)

BLANCO = (255, 255, 255)

class Personaje(pygame.sprite.Sprite):

    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("main-1.png")
        self.rect = self.image.get_rect()
        self.rect.x = largo_pantalla/2
        self.rect.y = alto_pantalla/2
        self.listaDisparo= []
        self.salud=2

    def mover_izq(self):
        self.rect.x-=20
    def mover_der(self):
        self.rect.x+=20
    def mover_arriba(self):
        self.rect.y-=20
    def mover_abajo(self):
        self.rect.y+=20 

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

class Espada(pygame.sprite.Sprite):

    def __init__(self, ancho1, alto1, posx, posy):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([ancho1, alto1])
        self.image.fill(ROJO)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    def atacar(self):
        while self.rect.y<=(protagonista.rect.y+50):
            self.rect.y+=5

        

class Enemigo(pygame.sprite.Sprite):

    def __init__(self, color, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.Surface([width, height])

        self.image.fill(color)

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.mover = False

        self.objetivo = None

    def resetear(self):
        self.rect.x = random.randrange(largo_pantalla)
        self.rect.y = random.randrange(alto_pantalla)
    
    def update(self):
 
        if self.mover == True:
            dx = self.objetivo[0] - self.rect.x
            dy = self.objetivo[1] - self.rect.y
            if abs(dx) > abs(dy):
                steps = abs(dx)
            else:
                steps = abs(dy)
            if steps > 0:
                xs = dx / steps
                ys = dy / steps
                self.rect.x += xs
                self.rect.y += ys

pygame.init()

largo_pantalla = 700
alto_pantalla = 400
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
fondo = pygame.image.load("montanas.jpg").convert()

bloque_lista = pygame.sprite.Group()

listade_todoslos_sprites= pygame.sprite.Group()

protagonista = Personaje(ROJO, 20, 15)

espada = Espada(50, 10, protagonista.rect.x-30, protagonista.rect.y+30)

enemigo = Enemigo(ROJO, 50, 50, 200, 100)

#proyectil1 = Proyectil(largo_pantalla/2, alto_pantalla/2)

listade_todoslos_sprites.add(protagonista)

listade_todoslos_sprites.add(espada)

listade_todoslos_sprites.add(enemigo)

bloque_lista.add(enemigo)

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
                espada.rect.x = protagonista.rect.x-30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
            if evento.key == pygame.K_RIGHT:
                protagonista.mover_der()
                espada.rect.x = protagonista.rect.x+45
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
            if evento.key == pygame.K_UP:
                protagonista.mover_arriba()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
            if evento.key == pygame.K_DOWN:
                protagonista.mover_abajo()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
            if evento.key == pygame.K_SPACE:
                espada.atacar()
            
    if protagonista.salud==0:
        listade_todoslos_sprites.remove(protagonista)
        listade_todoslos_sprites.remove(enemigo)
        listade_todoslos_sprites.remove(espada)

    pantalla.fill(BLANCO)

    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)

    lista_impactos_espada = pygame.sprite.spritecollide(espada, bloque_lista, False)

    for enemigo in lista_impactos_bloques:
        puntuacion+=1
        protagonista.salud-=1
        print(puntuacion)
        enemigo.resetear()

    for enemigo in lista_impactos_espada:
        puntuacion+=1
        print(puntuacion)
        enemigo.resetear()

    listade_todoslos_sprites.draw(pantalla)
      
    reloj.tick(30)

    pygame.display.flip()
  
pygame.quit()