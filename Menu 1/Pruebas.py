import pygame
import random

ROJO = (255, 0, 0)

BLANCO = (255, 255, 255)

NEGRO = (0,0,0)

AZUL = (0,0,255)

COLOR_VIDA=(0,255,0)

COLOR_MANA=(0,0,200)

COLOR_ORO=(100,200,0)

class Personaje(pygame.sprite.Sprite):

    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.image.load("movimiento1/stand.bmp")

        self.rect = self.image.get_rect()

        self.rect.x = largo_pantalla/2

        self.rect.y = alto_pantalla/2

        self.bucle_anim_izq = 0

        self.bucle_anim_der = 0

        self.bucle_anim_up = 0

        self.bucle_anim_down = 0

        self.movimiento = 0

        self.listaDisparo = []

        self.listaEspada = []

        self.salud = 3

        self.mana = 100

        self.oro = 0

        self.hitbox = (self.rect.x + 32, self.rect.y+5, 28, 60)

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
        lista_disparos.add(miProyectil)

    def atacar(self,x,y):
        pass

    def update(self):

        #Bucle de animación de caminar a la izquierda
        if self.bucle_anim_izq == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("movimiento1/main-walk-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("movimiento1/main-walk-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("movimiento1/main-walk-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("movimiento1/main-walk-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 5:
                self.image = pygame.image.load("movimiento1/main-walk-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 6:
                self.image = pygame.image.load("movimiento1/main-walk-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 7:
                self.image = pygame.image.load("movimiento1/main-walk-7.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1
        
            

        #Bucle de animación de caminar a la derecha 
        if self.bucle_anim_der == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("movimiento1/main-walk-right-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("movimiento1/main-walk-right-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("movimiento1/main-walk-right-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("movimiento1/main-walk-right-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 5:
                self.image = pygame.image.load("movimiento1/main-walk-right-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 6:
                self.image = pygame.image.load("movimiento1/main-walk-right-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 7:
                self.image = pygame.image.load("movimiento1/main-walk-right-7.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        #Bucle de animación de caminar hacia arriba
        if self.bucle_anim_up == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("movimiento1/walk_up_1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("movimiento1/walk_up_2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("movimiento1/walk_up_3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("movimiento1/walk_up_4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        #Bucle de animación para caminar hacia abajo
        if self.bucle_anim_down == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("movimiento1/walk_down_1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("movimiento1/walk_down_2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("movimiento1/walk_down_3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("movimiento1/walk_down_4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1
            
        if self.bucle_anim_der == 0 and self.bucle_anim_izq == 0 and self.bucle_anim_up == 0 and self.bucle_anim_down == 0:
            self.image = pygame.image.load("movimiento1/stand.bmp").convert()
            self.image.set_colorkey(BLANCO)

        pygame.draw.rect(pantalla, (255,0,0), self.hitbox, 2)


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

        self.velocidadEspada = 5
    
    def atacar(self):
      self.rect.y += self.velocidadEspada

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

class Vendedor(pygame.sprite.Sprite):

    def __init__(self, color, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.Surface([width, height])

        self.image.fill(color)

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.hitbox = [self.rect.x, self.rect.y, 50, 60]
    
    def update(self):

        pygame.draw.rect(pantalla, (255,0,0), self.hitbox, 2)



pygame.init()

largo_pantalla = 700

alto_pantalla = 400

pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])

h = 0

offset_x = 0

j = 0

offset_y = 0

imagen_fondo = pygame.image.load("montanas.jpg").convert()

fuente = pygame.font.Font(None, 30)

bloque_lista = pygame.sprite.Group()

vendedor_lista = pygame.sprite.Group()

listade_todoslos_sprites= pygame.sprite.Group()

protagonista = Personaje(ROJO, 20, 15)

protagonista.image.set_colorkey(BLANCO)

espada = Espada(50, 10, protagonista.rect.x-30, protagonista.rect.y+30)

enemigo = Enemigo(ROJO, 50, 50, 200, 100)

enemigo2 = Enemigo(ROJO, 50, 50, 300, 100)

vendedor1 = Vendedor(AZUL, 50,50,450,100)

vendedor2 = Vendedor(AZUL, 50,50,450,200)

listade_todoslos_sprites.add(protagonista)

listade_todoslos_sprites.add(espada)

listade_todoslos_sprites.add(enemigo)

listade_todoslos_sprites.add(enemigo2)

listade_todoslos_sprites.add(vendedor1)

listade_todoslos_sprites.add(vendedor2)

bloque_lista.add(enemigo2)

bloque_lista.add(enemigo)

vendedor_lista.add(vendedor1)

vendedor_lista.add(vendedor2)

lista_disparos=pygame.sprite.Group()

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
                offset_x = 1
                #protagonista.mover_izq()
                espada.rect.x = protagonista.rect.x-30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 1
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_RIGHT:
                indicador=2
                offset_x = -1
                #protagonista.mover_der()
                espada.rect.x = protagonista.rect.x+45
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
                protagonista.bucle_anim_der = 1
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_UP:
                indicador=3
                offset_y = 1
                #protagonista.mover_arriba()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 1
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_DOWN:
                indicador=4
                offset_y = -1
                #protagonista.mover_abajo()
                espada.rect.y = protagonista.rect.y+30
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                enemigo2.mover = True
                enemigo2.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 1
            if evento.key == pygame.K_SPACE:
                x,y=protagonista.rect.center
                protagonista.disparar(x,y)
            if evento.key == pygame.K_q:
                espada.atacar()
        if evento.type == pygame.KEYUP:
            offset_x = 0
            offset_y = 0
            protagonista.bucle_anim_izq = 0
            protagonista.bucle_anim_der = 0
            protagonista.bucle_anim_up = 0
            protagonista.bucle_anim_down = 0
            protagonista.movimiento = 0
                
    texto = fuente.render("Puntuacion: %d" % (puntuacion), 0, (255,255,255))

    salud = fuente.render("Salud: ", 0, (255,255,255))

    mana = fuente.render("Mana: %d" %(protagonista.mana), 0, (255,255,255))

    oro = fuente.render("Oro: %d" %(protagonista.oro), 0, (255,255,255))

    h+=offset_x

    j+=offset_y

    if h>=1 or h<=-279:
        offset_x=0

    if j>= 215 or j<=-400:
        offset_y=0

    pantalla.blit(imagen_fondo, [h,j])

    vendedor1.rect.x=450+h

    vendedor1.rect.y=100+j

    vendedor2.rect.x=450+h

    vendedor2.rect.y=200+j

    vendedor1.hitbox[0]=450+h

    vendedor1.hitbox[1]=50+j

    vendedor2.hitbox[0]=450+h

    vendedor2.hitbox[1]=200+j

    corazon1 = pygame.image.load("corazon1.png")

    corazon2 = pygame.image.load("corazon1.png")

    corazon3 = pygame.image.load("corazon1.png")

    corazon1.set_colorkey(BLANCO)

    corazon2.set_colorkey(BLANCO)

    corazon3.set_colorkey(BLANCO)

    pantalla.blit(texto, (20,20))

    pantalla.blit(salud, (510,20))

    pantalla.blit(mana, (510,50))

    pantalla.blit(oro, (510,80))

    if protagonista.salud==3:
    
        pantalla.blit(corazon1, (560, -5))

        pantalla.blit(corazon2, (590, -5))

        pantalla.blit(corazon3, (620,-5))

    if protagonista.salud==2:

        pantalla.blit(corazon1, (560, -5))

        pantalla.blit(corazon2, (590, -5))
    
    if protagonista.salud==1:

        pantalla.blit(corazon1, (560, -5))

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
        if x.rect.x > protagonista.rect.x+120:
            protagonista.listaDisparo.remove(x)
            protagonista.mana-=10
        
    if len(protagonista.listaDisparo)>0 and indicador==3:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_arriba()
        if x.rect.y < protagonista.rect.y-80:
            protagonista.listaDisparo.remove(x)
            protagonista.mana-=10
        
    if len(protagonista.listaDisparo)>0 and indicador==4:
        for x in protagonista.listaDisparo:
            x.dibujar(pantalla)
            x.disparo_abajo()
        if x.rect.y > protagonista.rect.y+80:
            protagonista.listaDisparo.remove(x)
            protagonista.mana-=10

    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, bloque_lista, False)

    lista_impactos_espada = pygame.sprite.spritecollide(espada, bloque_lista, False)

    lista_impactos_vendedor = pygame.sprite.spritecollide(vendedor1, vendedor_lista, False)

    for enemigo in lista_impactos_bloques:
        puntuacion+=1
        print(puntuacion)
        protagonista.oro+=10
        protagonista.salud-=1
        enemigo.resetear()

    for enemigo in lista_impactos_espada:
        puntuacion+=1
        print(puntuacion)
        protagonista.oro+=10
        enemigo.resetear()

    for enemigo2 in lista_impactos_bloques:
        puntuacion+=1
        print(puntuacion)
        protagonista.salud-=1
        protagonista.oro+=10
        enemigo.resetear()

    for enemigo2 in lista_impactos_espada:
        puntuacion+=1
        print(puntuacion)
        protagonista.oro+=10
        enemigo.resetear()

    for vendedor1 in lista_impactos_vendedor:

        offset_x = 0

        offset_y = 0
    
    for vendedor2 in lista_impactos_vendedor:

        offset_x = 0

        offset_y = 0
    
    if vendedor1.hitbox[0] < protagonista.hitbox[0]:

        print ("Contacto")
    
    listade_todoslos_sprites.draw(pantalla)
      
    reloj.tick(30)

    pygame.display.flip()
  
pygame.quit()