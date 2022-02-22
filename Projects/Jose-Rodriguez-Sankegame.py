import random
import pygame
import time
pygame.init() # inicia todos los médules de PuBame

pink = (240, 67, 223) #Score
orange = (240, 126, 41) #game over
red = (240, 64, 48) #food
green = (138, 245, 96) #pantalla
blue = (100, 190, 250) #snake

dis_width = 400
dis_height = 300
dis=pygame.display.set_mode((dis_width, dis_height))
pygame.display.update() #actualiza los cambios que ocurtan en la pantalla

pygame.display.set_caption("Snake game by JD") # ARaneserá el nombre del jusse
game_over=False

snake_block = 10
snake_speed = 25

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 25)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/7, dis_height/2])

def gameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) /10) *10
    foody = round(random.randrange(0, dis_width - snake_block) /10) *10


    while not game_over:

        while game_close == True:
            dis.fill(green)
            message("You lost. Press Q-Quit or P-Play Again", orange)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameRestart()

        for event in pygame.event.get():
            if event.type== pygame.QUIT: #cierra la pantalla al pinchar la (x))
                game_over=True
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_s:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block]) #crea el food
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block]) #crea el snake
        pygame.display.update()   

        clock.tick(snake_speed)

#pygame.display.update() 
#time.sleep(2) 
    pygame.quit() #termina todo
    quit()

gameRestart()