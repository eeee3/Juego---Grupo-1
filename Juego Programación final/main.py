import pygame
import random

pygame.init()



puntuacion = 0


NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

largo_pantalla=800
alto_pantalla=600

pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
pygame.display.set_caption("Bulov")

x = 0
offset_x = 0
y = 0
offset_y = 0


reloj = pygame.time.Clock()

hecho = False

class Personaje(pygame.sprite.Sprite):
    def __init__(self, ancho, alto):
        super().__init__()
        self.variable_arma = 0

        self.bucle_anim_izq = 0
        self.bucle_anim_der = 0
        self.bucle_anim_up = 0
        self.bucle_anim_down = 0

        self.attack_up_token = 0
        self.attack_down_token = 0
        self.attack_left_token = 0
        self.attack_right_token = 0

        self.arco_up_token = 0
        self.arco_down_token = 0
        self.arco_left_token = 0
        self.arco_right_token = 0

        self.ataque_bucle = 0
        self.ataque_arco = 0

        self.movimiento = 0

        self.oro = 0
        self.salud = 3
        self.flechas_disponibles = 10

        self.image = pygame.image.load("stand.bmp")
        self.image.set_colorkey(BLANCO)

        self.personaje_x = 0
        self.personaje_y = 0

        self.rect = self.image.get_rect()
        self.rect.x = largo_pantalla/2
        self.rect.y = alto_pantalla/2

        self.listaDisparo = []

        self.hitbox = [self.rect.x, self.rect.y-3, 28, 55]
    
    def disparar(self, h, j):

        miProyectil = Proyectil(h,j,20,20)
        self.listaDisparo.append(miProyectil)
        lista_disparos.add(miProyectil)

    def update(self):
        
        if self.bucle_anim_izq == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("main-walk-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("main-walk-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("main-walk-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("main-walk-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 5:
                self.image = pygame.image.load("main-walk-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 6:
                self.image = pygame.image.load("main-walk-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 7:
                self.image = pygame.image.load("main-walk-7.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        if self.bucle_anim_der == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load(
                    "main-walk-right-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load(
                    "main-walk-right-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load(
                    "main-walk-right-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load(
                    "main-walk-right-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 5:
                self.image = pygame.image.load(
                    "main-walk-right-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 6:
                self.image = pygame.image.load(
                    "main-walk-right-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 7:
                self.image = pygame.image.load(
                    "main-walk-right-7.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        if self.bucle_anim_up == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("walk_up_1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("walk_up_2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("walk_up_3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("walk_up_4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        if self.bucle_anim_down == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("walk_down_1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("walk_down_2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("walk_down_3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("walk_down_4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        if self.attack_up_token == 1:
            self.ataque_bucle += 1
            if self.ataque_bucle == 1:
                self.image = pygame.image.load("attack-back-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 2:
                self.image = pygame.image.load("attack-back-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 3:
                self.image = pygame.image.load("attack-back-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 4:
                self.image = pygame.image.load("attack-back-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 5:
                self.image = pygame.image.load("attack-back-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 6:
                self.image = pygame.image.load("attack-back-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.ataque_bucle = 0

        if self.attack_down_token == 1:
            self.ataque_bucle += 1
            if self.ataque_bucle == 1:
                self.image = pygame.image.load("attack-front-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 2:
                self.image = pygame.image.load("attack-front-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 3:
                self.image = pygame.image.load("attack-front-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 4:
                self.image = pygame.image.load("attack-front-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 5:
                self.image = pygame.image.load("attack-front-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 6:
                self.image = pygame.image.load("attack-front-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.ataque_bucle = 0

        if self.attack_right_token == 1:
            self.ataque_bucle += 1
            if self.ataque_bucle == 1:
                self.image = pygame.image.load("attack-1-right.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 2:
                self.image = pygame.image.load("attack-2-right.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 3:
                self.image = pygame.image.load("attack-3-right.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 4:
                self.image = pygame.image.load("attack-4-right.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.ataque_bucle = 0

        if self.attack_left_token == 1:
            self.ataque_bucle += 1
            if self.ataque_bucle == 1:
                self.image = pygame.image.load("attack-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 2:
                self.image = pygame.image.load("attack-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 3:
                self.image = pygame.image.load("attack-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_bucle == 4:
                self.image = pygame.image.load("attack-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.ataque_bucle = 0

        if self.bucle_anim_der == 0 and self.bucle_anim_izq == 0 and self.bucle_anim_up == 0 and self.bucle_anim_down == 0 and self.attack_up_token == 0 and self.attack_down_token == 0 and self.attack_right_token == 0 and self.attack_left_token == 0:
            self.image = pygame.image.load("stand.bmp").convert()
            self.image.set_colorkey(BLANCO)

class Proyectil(pygame.sprite.Sprite):
    def __init__(self, posx, posy, ancho1, alto1):
        pygame.sprite.Sprite.__init__(self)

        self.imageProyectil = pygame.image.load("flecha-der.bmp").convert()

        self.imageProyectil.set_colorkey(BLANCO)

        self.rect = self. imageProyectil.get_rect()

        self.velocidadDisparo = 20

        self.rect.top = posy

        self.rect.left = posx

    def disparo_arriba(self):

        self.imageProyectil = pygame.image.load("flecha-arriba.bmp").convert()

        self.imageProyectil.set_colorkey(BLANCO)

        self.rect.top = self.rect.top - self.velocidadDisparo
    
    def disparo_abajo(self):

        self.imageProyectil = pygame.image.load("flecha-arriba.bmp").convert()

        self.imageProyectil.set_colorkey(BLANCO)

        self.rect.y = self.rect.y + self.velocidadDisparo

    
    def disparo_izquierda(self):

        self.imageProyectil = pygame.image.load("flecha-der.bmp").convert()

        self.imageProyectil.set_colorkey(BLANCO)

        self.rect.left = self.rect.left - self.velocidadDisparo

    
    def disparo_derecha(self):
    
        self.imageProyectil = pygame.image.load("flecha-iz.bmp").convert()

        self.imageProyectil.set_colorkey(BLANCO)

        self.rect.x = self.rect.x + self.velocidadDisparo

    def dibujar(self, superficie):

        superficie.blit(self.imageProyectil, self.rect)

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, color, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.image.load("enemy.png")

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.mover = False

        self.objetivo = None

    def resetear(self):
        self.rect.x = random.randrange(800)

        self.rect.y = random.randrange(800)
    
    def update(self):
 
        if self.mover == True:
            self.rect.x += offset_x
            self.rect.y += offset_y

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

class Arbol(pygame.sprite.Sprite):
    def __init__(self, arbol_x, arbol_y):
        super().__init__()
        self.pic = random.randrange(1, 4)
        if self.pic == 1:
            self.image = pygame.image.load("arbol.bmp").convert()
        elif self.pic == 2:
            self.image = pygame.image.load("arbol2.bmp").convert()
        else:
            self.image = pygame.image.load("arbol3.bmp").convert()
        self.image.set_colorkey(BLANCO)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-200, 800)
        self.rect.y = random.randrange(-400, 0)
        self.offset_x = 0
        self.offset_y = 0

    def update(self):
        self.rect.x += offset_x
        self.rect.y += offset_y

class Vendedor(pygame.sprite.Sprite):

    def __init__(self, color, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.image.load("tienda.png")

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.hitbox = [self.rect.x, self.rect.y, 125, 120]
    
    def update(self):

        pass

class Pocion(pygame.sprite.Sprite):

    def __init__(self, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.image.load("Pocion.png")

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.hitbox = [self.rect.x, self.rect.y, 20, 20]
    
    def update(self):
        pass

class Flechas(pygame.sprite.Sprite):

    def __init__(self, width, height, posx, posy):

        super().__init__() 

        self.image = pygame.image.load("flecha-iz.bmp")

        self.image.set_colorkey(BLANCO)

        self.rect = self.image.get_rect()  

        self.rect.x = posx

        self.rect.y = posy

        self.hitbox = [self.rect.x, self.rect.y , 30, 20]
    
    def update(self):
        pass
 

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



arbol_lista = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()
lista_colisionables = pygame.sprite.Group()
listade_enemigos = pygame.sprite.Group()
lista_vendedor = pygame.sprite.Group()
lista_pocion = pygame.sprite.Group()
lista_flecha = pygame.sprite.Group()
lista_disparos=pygame.sprite.Group()

for i in range(random.randrange(5,20)):
    arbol = Arbol(x, y)

    arbol.rect.x = random.randrange(800)
    arbol.rect.y = random.randrange(200, 600)

    arbol_lista.add(arbol)
    lista_colisionables.add(arbol)
    

enemigo = Enemigo(ROJO, 50, 50, 200, 100)
enemigo2 = Enemigo(ROJO, 50, 50, 300, 100)
listade_enemigos.add(enemigo)
protagonista = Personaje(400, 400)
vendedor2 = Vendedor(BLANCO,50,50,450,200)
pocion = Pocion(60,60,470,330)
flechas = Flechas(60,60,530,20)
id_fondo1 = 0
id_interaccion1 = 0
id_interaccion2 = 0
identificador = 0
mifuente = pygame.font.Font(None, 60)
verificador = 0
puntuacion=0
play=pygame.image.load("play.jpeg")
play1=pygame.image.load("play1.jpeg")
quit1=pygame.image.load("quit.jpeg")
quit2=pygame.image.load("quit1.jpeg")
fuente = pygame.font.Font(None, 20)
boton1=Boton(play,play1,310,300)
boton2=Boton(quit1,quit2,310,450)
imagen_fondo1 = pygame.image.load("menu2.png")
cursor1=Cursor()
pantalla.blit(imagen_fondo1, [x,y])
if puntuacion == 100 :
    enemigo3 = Enemigo(ROJO, 50, 50, 300, 100)
    listade_todoslos_sprites.add(enemigo3)
    listade_enemigos.add(enemigo3)
if puntuacion == 150:
    enemigo4 = Enemigo(ROJO, 50, 50, 600, 100)
    listade_todoslos_sprites.add(enemigo4)
    listade_enemigos.add(enemigo4)
if puntuacion == 200:
    enemigo5 = Enemigo(ROJO, 50, 50, 500, 100)
    listade_todoslos_sprites.add(enemigo5)
    listade_enemigos.add(enemigo5)



while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                offset_x = -4
                identificador = 2
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                protagonista.bucle_anim_der = 1
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_LEFT:
                offset_x = 4
                identificador = 1
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 1
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_DOWN:
                offset_y = -4
                identificador = 4
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 1
            if evento.key == pygame.K_UP:
                offset_y = 4
                identificador = 3
                pos=[protagonista.rect.x, protagonista.rect.y]
                enemigo.mover = True
                enemigo.objetivo = pos
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 1
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_w:
                if protagonista.variable_arma == 0:
                    protagonista.attack_up_token = 1
                    protagonista.attack_down_token = 0
                    protagonista.attack_left_token = 0
                    protagonista.attack_right_token = 0
                elif protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 1
                    protagonista.arco_down_token = 0
                    protagonista.arco_left_token = 0
                    protagonista.arco_right_token = 0
                else:
                    protagonista.attack_up_token = 1
                    protagonista.attack_down_token = 0
                    protagonista.attack_left_token = 0
                    protagonista.attack_right_token = 0
            if evento.key == pygame.K_a:
                if protagonista.variable_arma == 0:
                    protagonista.attack_up_token = 0
                    protagonista.attack_down_token = 0
                    protagonista.attack_left_token = 1
                    protagonista.attack_right_token = 0
                if protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 0
                    protagonista.arco_down_token = 0
                    protagonista.arco_left_token = 1
                    protagonista.arco_right_token = 0
            if evento.key == pygame.K_d:
                if protagonista.variable_arma == 0:
                    protagonista.attack_up_token = 0
                    protagonista.attack_down_token = 0
                    protagonista.attack_left_token = 0
                    protagonista.attack_right_token = 1
                elif protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 0
                    protagonista.arco_down_token = 0
                    protagonista.arco_left_token = 0
                    protagonista.arco_right_token = 1
                else:
                    protagonista.attack_up_token = 0
                    protagonista.attack_down_token = 0
                    protagonista.attack_left_token = 0
                    protagonista.attack_right_token = 1
            if evento.key == pygame.K_s:
                if protagonista.variable_arma == 0:
                    protagonista.attack_up_token = 0
                    protagonista.attack_down_token = 1
                    protagonista.attack_left_token = 0
                    protagonista.attack_right_token = 0
                if protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 0
                    protagonista.arco_down_token = 1
                    protagonista.arco_left_token = 0
                    protagonista.arco_right_token = 0
            if evento.key == pygame.K_z:
                if protagonista.variable_arma == 0:
                    protagonista.variable_arma += 1
                else:
                    protagonista.variable_arma = 0
            if evento.key == pygame.K_e:
                if protagonista.rect.colliderect(pocion.rect) and protagonista.oro >= 30 and protagonista.salud < 3:
                    protagonista.oro -= 30
                    protagonista.salud += 1
                if protagonista.rect.colliderect(flechas.rect) and protagonista.oro >= 10:
                    protagonista.oro -= 10
                    protagonista.flechas_disponibles+= 1
            if evento.key == pygame.K_SPACE:
                if protagonista.flechas_disponibles > 0:
                    h,j=protagonista.rect.center
                    protagonista.disparar(h,j)
                    protagonista.flechas_disponibles -= 1


        if evento.type == pygame.KEYUP:
            offset_x = 0
            offset_y = 0
            protagonista.bucle_anim_izq = 0
            protagonista.bucle_anim_der = 0
            protagonista.bucle_anim_up = 0
            protagonista.bucle_anim_down = 0
            protagonista.attack_up_token = 0
            protagonista.attack_down_token = 0
            protagonista.attack_left_token = 0
            protagonista.attack_right_token = 0
            protagonista.arco_up_token = 0
            protagonista.arco_down_token = 0
            protagonista.arco_left_token = 0
            protagonista.arco_right_token = 0
            protagonista.movimiento = 0
        
        if evento.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    verificador = 1
                    listade_todoslos_sprites.add(protagonista)
                    listade_todoslos_sprites.add(enemigo)
                    listade_todoslos_sprites.add(vendedor2)
                    listade_todoslos_sprites.add(flechas)
                    listade_todoslos_sprites.add(pocion)
                    listade_enemigos.add(enemigo)
                    lista_flecha.add(flechas)
                    lista_pocion.add(pocion)
                    lista_vendedor.add(vendedor2)
                    id_fondo1 = 1
                    for arbol in arbol_lista:
                        listade_todoslos_sprites.add(arbol)

                if cursor1.colliderect(boton2.rect):
                    hecho=True


    x += offset_x
    y += offset_y

    if x >= 1 or x <= -279:
        offset_x = 0
    if y >= 100 or y <= -400:
        offset_y = 0

    vendedor2.rect.x=450+x

    vendedor2.rect.y=200+y

    vendedor2.hitbox[0]=450+x

    vendedor2.hitbox[1]=200+y

    pocion.rect.x=470+x

    pocion.rect.y=330+y

    pocion.hitbox[0]=470+x

    pocion.hitbox[1]=330+y

    flechas.rect.x=530+x

    flechas.rect.y=335+y

    flechas.hitbox[0]=530+x

    flechas.hitbox[1]=330+y

    oro_texto = fuente.render("Oro = " + str(protagonista.oro), 1, (0,0,0))
    puntuacion_texto = fuente.render("Puntos = " + str(puntuacion), 1, (0,0,0))
    flechas_disponibles = fuente.render("Flechas = "+str(protagonista.flechas_disponibles),1,(0,0,0))
    pocion_coste = fuente.render("30 oro",1,(0,0,0))
    flechas_coste = fuente.render("10 oro",1,(0,0,0))
    game_over = fuente.render("Game Over",1,(255,255,255))
    mitexto = mifuente.render("Game Over",0,(255,255,255))

    for arbol in arbol_lista:
        arbol.offset_x = offset_x
        arbol.offset_y = offset_y
        arbol.update()

    listade_todoslos_sprites.update()

    lista_impactos_bloques = pygame.sprite.spritecollide(protagonista, listade_enemigos, False)
    lista_impactos_vendedor = pygame.sprite.spritecollide(protagonista, lista_vendedor, False)
    lista_impactos_pocion = pygame.sprite.spritecollide(protagonista, lista_pocion, False)
    lista_impactos_flechas = pygame.sprite.spritecollide(protagonista, lista_flecha, False)

    if len(lista_impactos_bloques) > 0:
        offset_x = 0
        offset_y = 0
    
    for enemigo in lista_impactos_bloques:
        if protagonista.attack_up_token == 1 or protagonista.attack_right_token == 1 or protagonista.attack_left_token == 1 or protagonista.attack_down_token == 1:
            enemigo.resetear()
            protagonista.oro += 10
            puntuacion+=10
        else:
            protagonista.salud -= 1
            enemigo.resetear()

    if protagonista.rect.colliderect(vendedor2.rect):
        offset_x = 0
        offset_y = 0
    
    if protagonista.rect.colliderect(pocion.rect):
        offset_x = 0
        offset_y = 0
        id_interaccion1 = 1
    
    if protagonista.rect.colliderect(flechas.rect):
        offset_x = 0
        offset_y = 0
    
    listade_todoslos_sprites.update()

    corazon1 = pygame.image.load("corazon1 (1).bmp")

    corazon2 = pygame.image.load("corazon1 (1).bmp")

    corazon3 = pygame.image.load("corazon1 (1).bmp")

    imagen_de_fondo = pygame.image.load("fondo.png").convert()

    fondo_gameover = pygame.image.load("negro.jpg").convert()

    corazon1.set_colorkey(BLANCO)

    corazon2.set_colorkey(BLANCO)

    corazon3.set_colorkey(BLANCO)

    arbol.update()

    if id_fondo1 == 1 :

        pantalla.blit(imagen_de_fondo, [x,y])

        pantalla.blit(oro_texto,(700,80))

        pantalla.blit(puntuacion_texto,(700,100))

        pantalla.blit(flechas_disponibles,(700,120))

        pantalla.blit(pocion_coste,(460+x,360+y))

        pantalla.blit(flechas_coste,(525+x,360+y))

        if protagonista.salud == 3:

            pantalla.blit(corazon1, (620,20))

            pantalla.blit(corazon2, (670,20))

            pantalla.blit(corazon3, (720,20))
        
        if protagonista.salud == 2:

            pantalla.blit(corazon2, (670,20))

            pantalla.blit(corazon3, (720,20))
        
        if protagonista.salud == 1:

            pantalla.blit(corazon3, (720,20))
    
    if protagonista.salud == 0:
        id_fondo = 0
        listade_todoslos_sprites.remove(protagonista)
        listade_todoslos_sprites.remove(enemigo)
        listade_todoslos_sprites.remove(vendedor2)
        listade_todoslos_sprites.remove(flechas)
        listade_todoslos_sprites.remove(pocion)
        pantalla.blit(fondo_gameover, (0,0))
        pantalla.blit(mitexto,(300,250))
        verificador = 3

    cursor1.update()

    if verificador == 0:

        boton1.update(pantalla, cursor1)
        boton2.update(pantalla, cursor1)
    
    if verificador == 3:

        boton2.update(pantalla,cursor1)
    
    if len(protagonista.listaDisparo)>0 and identificador==1:
        for h in protagonista.listaDisparo:
            h.dibujar(pantalla)
            h.disparo_izquierda()
            if h.rect.x < protagonista.rect.x-150:
                protagonista.listaDisparo.remove(h)
            if h.rect.colliderect(enemigo.rect):
                protagonista.oro += 10
                puntuacion+=10
                enemigo.resetear()
                if len(protagonista.listaDisparo)>0:
                    protagonista.listaDisparo.remove(h)
                

    if len(protagonista.listaDisparo)>0 and identificador==2:
        for h in protagonista.listaDisparo:
            h.dibujar(pantalla)
            h.disparo_derecha()
            if h.rect.x > protagonista.rect.x+178:
                protagonista.listaDisparo.remove(h)
            if h.rect.colliderect(enemigo.rect):
                if len(protagonista.listaDisparo)>0:
                    protagonista.listaDisparo.remove(h)
                protagonista.oro += 10
                puntuacion+=10
                enemigo.resetear()
                
        
    if len(protagonista.listaDisparo)>0 and identificador==3:
        for h in protagonista.listaDisparo:
            h.dibujar(pantalla)
            h.disparo_arriba()
            if h.rect.y < protagonista.rect.y-150:
                protagonista.listaDisparo.remove(h)
            if h.rect.colliderect(enemigo.rect):
                if len(protagonista.listaDisparo)>0:
                    protagonista.listaDisparo.remove(h)
                protagonista.oro += 10
                puntuacion+=10
                enemigo.resetear()
                
        
    if len(protagonista.listaDisparo)>0 and identificador==4:
        for h in protagonista.listaDisparo:
            h.dibujar(pantalla)
            h.disparo_abajo()
            if h.rect.y > protagonista.rect.y+210:
                protagonista.listaDisparo.remove(h)
            if h.rect.colliderect(enemigo.rect):
                if len(protagonista.listaDisparo)>0:
                    protagonista.listaDisparo.remove(h)
                protagonista.oro += 10
                puntuacion+=10
                enemigo.resetear()
                


    listade_todoslos_sprites.draw(pantalla)

    listade_todoslos_sprites.update()

    pygame.display.flip()

    reloj.tick(60)


pygame.quit()