import pygame
import random

pygame.init()

# Definimos los colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)


# Definimos eltamaño de la pantalla

pantalla = pygame.display.set_mode([800, 800])

# Definimos el fondo

imagen_de_fondo = pygame.image.load("fondo.png").convert()

# Definimos las variables que van a mover el fondo cuando el personaje se nueva.

x = 0
offset_x = 0
y = 0
offset_y = 0


# Definimos el reloj

reloj = pygame.time.Clock()

hecho = False

# Definimos la clase del personaje principal como herencia de sprite.


class Personaje(pygame.sprite.Sprite):
    def __init__(self, personaje_x, personaje_y):
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

        self.image = pygame.image.load("stand.bmp").convert()
        self.image.set_colorkey(BLANCO)

        self.personaje_x = 0
        self.personaje_y = 0

        self.rect = self.image.get_rect()
        self.rect.x = personaje_x
        self.rect.y = personaje_y

    # La sección update se va a actualizar en cada leída de código. Por ende, acá van los cambios de sprite.

    def update(self):

        # Bucle de animación de caminar a la izquierda
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

        # Bucle de animación de caminar a la derecha
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

        # Bucle de animación de caminar hacia arriba
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

        # Bucle de animación para caminar hacia abajo
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
            print(self.ataque_bucle)
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

        if self.arco_left_token == 1:
            self.ataque_arco += 1
            if self.ataque_arco == 1:
                self.image = pygame.image.load("arco-iz-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 2:
                self.image = pygame.image.load("arco-iz-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 3:
                self.image = pygame.image.load("arco-iz-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 4:
                self.image = pygame.image.load("arco-iz-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else: 
                self.ataque_arco = 1

        if self.arco_right_token == 1:
            self.ataque_arco += 1
            print(self.ataque_arco)
            if self.ataque_arco == 1:
                self.image = pygame.image.load("arco-der-1.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 2:
                self.image = pygame.image.load("arco-der-2.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 3:
                self.image = pygame.image.load("arco-der-3.bmp").convert()
                self.image.set_colorkey(BLANCO)
            elif self.ataque_arco == 4:
                self.image = pygame.image.load("arco-der-4.bmp").convert()
                self.image.set_colorkey(BLANCO)
            else: 
                self.ataque_arco = 1

        if self.bucle_anim_der == 0 and self.bucle_anim_izq == 0 and self.bucle_anim_up == 0 and self.bucle_anim_down == 0 and self.attack_up_token == 0 and self.attack_down_token == 0 and self.attack_right_token == 0 and self.attack_left_token == 0:
            self.image = pygame.image.load("stand.bmp").convert()
            self.image.set_colorkey(BLANCO)


# Creamos la clase Árbol
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


# Añadimos los sprites a las listas correspondientes.
arbol_lista = pygame.sprite.Group()
listade_todoslos_sprites = pygame.sprite.Group()
lista_colisionables = pygame.sprite.Group()

# Creamos los árboles
for i in range(random.randrange(5, 20)):
    # Esto representa un arbol
    arbol = Arbol(x, y)

    # Establece una ubicación aleatoria para el arbol
    arbol.rect.x = random.randrange(800)
    arbol.rect.y = random.randrange(200, 600)

    # Añade el arbol a la lista de objetos

    arbol_lista.add(arbol)
    lista_colisionables.add(arbol)
    listade_todoslos_sprites.add(arbol)

# Creamos un objeto protagonista de la clase del personaje.
protagonista = Personaje(400, 400)
listade_todoslos_sprites.add(protagonista)

# En un bucle infinito configuramos las teclas.
while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RIGHT:
                offset_x = -4
                # bucle de animación del personaje
                protagonista.bucle_anim_der = 1
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_LEFT:
                offset_x = 4
                # bucle de animación del personaje
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 1
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 0
            if evento.key == pygame.K_DOWN:
                offset_y = -4
                # bucle de animación del personaje
                protagonista.bucle_anim_der = 0
                protagonista.bucle_anim_izq = 0
                protagonista.bucle_anim_up = 0
                protagonista.bucle_anim_down = 1
            if evento.key == pygame.K_UP:
                offset_y = 4
                # bucle de animación del personaje
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
                if protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 1
                    protagonista.arco_down_token = 0
                    protagonista.arco_left_token = 0
                    protagonista.arco_right_token = 0
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
                if protagonista.variable_arma == 1:
                    protagonista.arco_up_token = 0
                    protagonista.arco_down_token = 0
                    protagonista.arco_left_token = 0
                    protagonista.arco_right_token = 1
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


# Definimos el offset del movimiento de la pantalla definido anteriormente.

    x += offset_x
    y += offset_y

    if x >= 1 or x <= -279:
        offset_x = 0
    if y >= 215 or y <= -400:
        offset_y = 0

    for arbol in arbol_lista:
        arbol.offset_x = offset_x
        arbol.offset_y = offset_y

    listade_todoslos_sprites.update()

    # Definimos las colisiones
    # Observamos si el bloque protagonista ha colisionado con algo.
    lista_impactos_bloques = pygame.sprite.spritecollide(
        protagonista, arbol_lista, False)
    # Verificador de impacto
    if len(lista_impactos_bloques) > 0:
        offset_x = 0
        offset_y = 0
    # Copia la imagen en pantalla:
    pantalla.blit(imagen_de_fondo, [x, y])

    listade_todoslos_sprites.draw(pantalla)

    pygame.display.flip()

    reloj.tick(30)

pygame.quit()
