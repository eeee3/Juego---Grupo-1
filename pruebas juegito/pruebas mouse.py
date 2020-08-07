import pygame
import random
   
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
class Bloque(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
       
    
        super().__init__() 
  
     
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
  
      
        self.rect = self.image.get_rect()
        self.objetivo = None
         
    def update(self):
        
 
        dx = self.objetivo[0] - self.rect.x
        dy = self.objetivo[1] - self.rect.y
        if abs(dx) > abs(dy):
            steps = abs(dx)
        else:
            steps = abs(dy)
        print(steps)
        if steps > 0:
            xs = dx / steps
            ys = dy / steps
            print("{} {}".format(xs, ys))
            self.rect.x += xs
            self.rect.y += ys
pygame.init()
largo_pantalla = 700
alto_pantalla = 400
pantalla = pygame.display.set_mode([largo_pantalla, alto_pantalla])
listade_todoslos_sprites= pygame.sprite.Group()
bloque = Bloque(BLANCO, 20, 15)​
bloque.rect.x = random.randrange(largo_pantalla)
bloque.rect.y = random.randrange(alto_pantalla)
listade_todoslos_sprites.add(bloque)
hecho = False
reloj = pygame.time.Clock()
puntuacion = 0
while not hecho:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            hecho = True
    pos = pygame.mouse.get_pos()
    print(pos)
    bloque.objetivo = pos
    pantalla.fill(NEGRO)
    listade_todoslos_sprites.update()
    listade_todoslos_sprites.draw(pantalla)
    reloj.tick(60)
    pygame.display.flip()
  
pygame.quit()