import pygame
import random

pygame.init()

#Definimos los colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)


#Definimos eltamaño de la pantalla

pantalla = pygame.display.set_mode([800, 800])

#Definimos el fondo

imagen_de_fondo = pygame.image.load("fondo.png").convert()

#Definimos las variables que van a mover el fondo cuando el personaje se nueva.

x = 0
offset_x = 0
y = 0
offset_y = 0

#Definimos el reloj

reloj = pygame.time.Clock()

hecho = False

#Definimos la clase del personaje principal como herencia de sprite.

class Personaje(pygame.sprite.Sprite):
    def __init__(self, personaje_x, personaje_y):
        super().__init__()
        self.bucle_anim_izq = 0
        self.bucle_anim_der = 0
        self.bucle_anim_up = 0
        self.bucle_anim_down = 0
        self.movimiento = 0
        self.image = pygame.image.load("stand.bmp").convert()
        self.image.set_colorkey(BLANCO)
        self.personaje_x = 0
        self.personaje_y = 0
        self.rect = self.image.get_rect()
        self.rect.x = personaje_x
        self.rect.y = personaje_y

    #La sección update se va a actualizar en cada leída de código. Por ende, acá van los cambios de sprite.
    
    def update(self):
        
        #Bucle de animación de caminar a la izquierda
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
        
            

        #Bucle de animación de caminar a la derecha 
        if self.bucle_anim_der == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("main-walk-right-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 2:
                self.image = pygame.image.load("main-walk-right-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 3:
                self.image = pygame.image.load("main-walk-right-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 4:
                self.image = pygame.image.load("main-walk-right-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 5:
                self.image = pygame.image.load("main-walk-right-5.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 6:
                self.image = pygame.image.load("main-walk-right-6.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.movimiento == 7:
                self.image = pygame.image.load("main-walk-right-7.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else:
                self.movimiento = 1

        #Bucle de animación de caminar hacia arriba
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

        #Bucle de animación para caminar hacia abajo
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

        
        if self.bucle_anim_der == 0 and self.bucle_anim_izq == 0 and self.bucle_anim_up == 0 and self.bucle_anim_down == 0:
            self.image = pygame.image.load("stand.bmp").convert()
            self.image.set_colorkey(BLANCO)

#Creamos la clase Árbol
class Arbol(pygame.sprite.Sprite):
    def __init__(self, arbol_x, arbol_y):
        super().__init__()
        self.image = pygame.image.load("arbol.bmp").convert()
        self.image.set_colorkey(BLANCO)
        self.arbol_x = 450
        self.arbol_y = 450
        self.rect = self.image.get_rect()
        self.rect.x = arbol_x
        self.rect.y = arbol_y
    
#   def update(self):
        self.arbol_x += offset_x
        self.arbol_y += offset_y




#Creamos un objeto protagonista de la clase del personaje.

protagonista = Personaje(350,400)

#Creamos los árboles

arbol = Arbol(x+200, y+200)



#Añadimos los sprites a las listas correspondientes.

lista_personaje = pygame.sprite.Group()
lista_personaje.add(protagonista)
listade_todoslos_sprites = pygame.sprite.Group()
listade_todoslos_sprites.add(protagonista)
listade_todoslos_sprites.add(arbol)

#En un bucle infinito configuramos las teclas.

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                offset_x = -1
                protagonista.bucle_anim_der = 1
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_LEFT:
                offset_x = 1
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 1
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_DOWN:
                offset_y = -1
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 1
            if evento.key == pygame.K_UP:
                offset_y = 1
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 1
                protagonista.bucle_anim_down = 0
        if evento.type == pygame.KEYUP:
            offset_x = 0
            offset_y = 0
            protagonista.bucle_anim_izq = 0
            protagonista.bucle_anim_der = 0
            protagonista.bucle_anim_up = 0
            protagonista.bucle_anim_down = 0
            protagonista.movimiento = 0



#Definimos el offset del movimiento de la pantalla definido anteriormente.

    x += offset_x
    y += offset_y

    if x >= 1 or x <= -279:
        offset_x = 0
    if y >= 215 or y <= -400:
        offset_y = 0



    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, [x, y])
    arbol.rect = [x, y]
    
    listade_todoslos_sprites.update()

    listade_todoslos_sprites.draw(pantalla)
    

    pygame.display.flip()

    reloj.tick(30)

pygame.quit()