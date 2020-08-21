import pygame
import random

ROJO = (255, 0, 0)

BLANCO = (255, 255, 255)

NEGRO = (0,0,0)

AZUL = (0,0,255)

class Personaje(pygame.sprite.Sprite):

    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("main-1.png")

        self.rect = self.image.get_rect()

        self.rect.x = largo_pantalla/2

        self.rect.y = alto_pantalla/2

        self.listaDisparo= []

        self.salud=3

    def mover_izq(self):

        self.rect.x-=20

    def mover_der(self):

        self.rect.x+=20

    def mover_arriba(self):

        self.rect.y-=20

    def mover_abajo(self):

        self.rect.y+=20 

    def disparar(self, x, y):

        miProyectil = Proyectil(x,y,20,20)
        self.listaDisparo.append(miProyectil)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ancho1, alto1):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil = pygame.Surface([ancho1, alto1])

        self.imageProyectil.fill(AZUL)

        self.rect = self. imageProyectil.get_rect()

        self.velocidadDisparo = 5

        self.rect.top = posy

        self.rect.left = posx

    def disparo_arriba(self):

        self.rect.top = self.rect.top - self.velocidadDisparo
    
    def disparo_abajo(self):

        self.rect.y = self.rect.y + self.velocidadDisparo
    
    def disparo_izquierda(self):

        self.rect.left = self.rect.left - self.velocidadDisparo
    
    def disparo_derecha(self):

        self.rect.x = self.rect.x + self.velocidadDisparo

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
      pass  

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

fuente = pygame.font.Font(None, 30)

bloque_lista = pygame.sprite.Group()

listade_todoslos_sprites= pygame.sprite.Group()

proyectil1= Proyectil(largo_pantalla/2, alto_pantalla-20, 20, 20)

protagonista = Personaje(ROJO, 20, 15)

protagonista.image.set_colorkey(BLANCO)

espada = Espada(50, 10, protagonista.rect.x-30, protagonista.rect.y+30)

enemigo = Enemigo(ROJO, 50, 50, 200, 100)

enemigo2 = Enemigo(ROJO, 50, 50, 300, 100)

listade_todoslos_sprites.add(protagonista)

listade_todoslos_sprites.add(espada)

listade_todoslos_sprites.add(enemigo)

listade_todoslos_sprites.add(enemigo2)

bloque_lista.add(enemigo2)

bloque_lista.add(enemigo)

hecho = False

reloj = pygame.time.Clock()
  
puntuacion = 0

indicador=0

while not hecho:

    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                indicador=1
                protagonista.mover_izq()
                espada.rect.x = protagonista.rect.x-30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
            if evento.key == pygame.K_RIGHT:
                indicador=2
                protagonista.mover_der()
                espada.rect.x = protagonista.rect.x+45
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
            if evento.key == pygame.K_UP:
                indicador=3
                protagonista.mover_arriba()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
            if evento.key == pygame.K_DOWN:
                indicador=4
                protagonista.mover_abajo()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
            if evento.key == pygame.K_SPACE:
                x,y=protagonista.rect.center
                protagonista.disparar(x,y)
                    
    if protagonista.salud==0:
        listade_todoslos_sprites.remove(protagonista)
        listade_todoslos_sprites.remove(enemigo)
        listade_todoslos_sprites.remove(espada)

    pantalla.fill(NEGRO)

    texto = fuente.render("Puntuacion: %d" % (puntuacion), 0, (255,255,255))

    fondo = pygame.image.load("montanas.jpg")

    corazon1 = pygame.image.load("corazon1.png")

    corazon2 = pygame.image.load("corazon1.png")

    corazon3 = pygame.image.load("corazon1.png")

    corazon1.set_colorkey(BLANCO)

    pantalla.blit(fondo, (0,0))

    pantalla.blit(texto, (20,20))
    
    pantalla.blit(corazon1, (200, 20))

    if len(protagonista.listaDisparo)>0 and indicador==1:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_izquierda()
        if x.rect.x < protagonista.rect.x-80:
            protagonista.listaDisparo.remove(x)
        
    if len(protagonista.listaDisparo)>0 and indicador==2:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_derecha()
        if x.rect.x > protagonista.rect.x+80:
            protagonista.listaDisparo.remove(x)
        
    if len(protagonista.listaDisparo)>0 and indicador==3:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_arriba()
        if x.rect.y < protagonista.rect.y-80:
            protagonista.listaDisparo.remove(x)
        
    if len(protagonista.listaDisparo)>0 and indicador==4:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_abajo()
        if x.rect.y > protagonista.rect.y+80:
            protagonista.listaDisparo.remove(x)

    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)

    lista_impactos_espada = pygame.sprite.spritecollide(espada, bloque_lista, False)

    for enemigo in lista_impactos_bloques:
        puntuacion+=1
        print(puntuacion)
        enemigo.resetear()

    for enemigo in lista_impactos_espada:
        puntuacion+=1
        print(puntuacion)
        enemigo.resetear()

    for enemigo2 in lista_impactos_bloques:
        puntuacion+=1
        print(puntuacion)
        enemigo.resetear()

    for enemigo2 in lista_impactos_espada:
        puntuacion+=1
        print(puntuacion)
        enemigo.resetear()
    
    listade_todoslos_sprites.draw(pantalla)
      
    reloj.tick(30)

    pygame.display.flip()
  
pygame.quit()