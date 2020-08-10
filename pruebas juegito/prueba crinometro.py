import pygame
  

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
  
pygame.init()
   
   

dimensiones = [700, 500]
pantalla = pygame.display.set_mode(dimensiones)
  
pygame.display.set_caption("Mi Juego")
  

hecho = False
  

reloj = pygame.time.Clock()
 

fuente = pygame.font.Font(None, 25)
 
numero_de_fotogramas = 0
tasa_fotogramas = 60
instante_de_partida = 90
 

while not hecho:    
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True               
  
   
    pantalla.fill(BLANCO)
  
    
     
    segundos_totales = numero_de_fotogramas // tasa_fotogramas
     
    
    minutos = segundos_totales // 60
     
    
    segundos = segundos_totales % 60
     
    
    texto_de_salida = "Time: {0:02}:{1:02}".format(minutos, segundos)
     
    
    texto = fuente.render(texto_de_salida, True, NEGRO)
    pantalla.blit(texto, [250, 250])
     
    segundos_totales = instante_de_partida - (numero_de_fotogramas // tasa_fotogramas)
    if segundos_totales < 0:
        segundos_totales = 0
     
    minutos = segundos_totales // 60
     
    segundos = segundos_totales % 60
     
    texto_de_salida = "Time left: {0:02}:{1:02}".format(minutos, segundos)
     
    texto = fuente.render(texto_de_salida, True, NEGRO)
     
    pantalla.blit(texto, [250, 280])
     
    numero_de_fotogramas += 1
     
    reloj.tick(20)
  
    pygame.display.flip()
pygame.quit()