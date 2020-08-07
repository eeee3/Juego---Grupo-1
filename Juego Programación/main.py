import pygame

pygame.init()

#Definimos los colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)


#Definimos eltamaño de la pantalla

pantalla = pygame.display.set_mode([400, 400])

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
        self.bucle_anim = 0
        self.movimiento = 0
        self.image = pygame.image.load("stand.bmp").convert()
        self.image.set_colorkey(BLANCO)
        self.personaje_x = 0
        self.personaje_y = 0
        self.rect = self.image.get_rect()
        self.rect.x = personaje_x
        self.rect.y = personaje_y

    def update(self):
        if self.bucle_anim == 1:
            self.movimiento += 1
            if self.movimiento == 1:
                self.image = pygame.image.load("main-walk-1.bmp").convert()
            elif self.movimiento == 2:
                self.image = pygame.image.load("main-walk-2.bmp").convert()
            elif self.movimiento == 3:
                self.image = pygame.image.load("main-walk-3.bmp").convert()
            elif self.movimiento == 4:
                self.image = pygame.image.load("main-walk-4.bmp").convert()
            elif self.movimiento == 5:
                self.image = pygame.image.load("main-walk-5.bmp").convert()
            elif self.movimiento == 6:
                self.image = pygame.image.load("main-walk-6.bmp").convert()
            elif self.movimiento == 7:
                self.image = pygame.image.load("main-walk-7.bmp").convert()
            else:
                self.movimiento = 1
        else:
            self.image = pygame.image.load("stand.bmp").convert()

        

#Creamos un objeto protagonista de la clase del personaje.

protagonista = Personaje(170,200)


#Añadimos los sprites a las listas correspondientes.

lista_personaje = pygame.sprite.Group()
lista_personaje.add(protagonista)
listade_todoslos_sprites = pygame.sprite.Group()
listade_todoslos_sprites.add(protagonista)

#En un bucle infinito configuramos las teclas.

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                offset_x = -1
            if evento.key == pygame.K_LEFT:
                offset_x = 1
                protagonista.bucle_anim +=1
            if evento.key == pygame.K_DOWN:
                offset_y = -1
            if evento.key == pygame.K_UP:
                offset_y = 1
        if evento.type == pygame.KEYUP:
            offset_x = 0
            offset_y = 0
            protagonista.bucle_anim = 0

#Definimos el offset del movimiento de la pantalla definido anteriormente.

    x += offset_x
    y += offset_y

    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, [x, y])
    
    listade_todoslos_sprites.update()

    listade_todoslos_sprites.draw(pantalla)
    

    pygame.display.flip()

    reloj.tick(60)

pygame.quit()