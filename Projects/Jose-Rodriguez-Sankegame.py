from dis import dis
import pygame
pygame.init() # inicia todos los médules de PuBame

yellow = (255, 255, 102) #Score
black = (0, 0, 0) #pantalla
red = (213, 50, 80) #game over
green = (0, 255, 0) #food
blue = (50, 153, 213) #snake

dis-pygame.display.set_mode((400,300))
pygame.display.update() #actualiza los cambios que ocurtan en la pantalla
pygame.display.set_caption("Snake game by JD") # ARaneserá el nombre del jusse
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: #cierra la pantalla al pinchar la (x))
            game_over=True
           
pygame.quit() #termina todo
quit()