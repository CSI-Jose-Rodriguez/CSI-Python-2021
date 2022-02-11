import pygame
pygame.init() # inicia todos los médules de PuBame

pink = (240, 67, 223) #Score
orange = (240, 126, 41) #game over
red = (240, 64, 48) #food
green = (138, 245, 96) #pantalla
blue = (100, 190, 250) #snake

dis=pygame.display.set_mode((500,400))
pygame.display.update() #actualiza los cambios que ocurtan en la pantalla
pygame.display.set_caption("Snake game by JD") # ARaneserá el nombre del jusse
game_over=False

x1 = 250
y1 = 200

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type== pygame.QUIT: #cierra la pantalla al pinchar la (x))
            game_over=True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_a:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_w:
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_s:
                x1_change = 0
                y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill(green)

    pygame.draw.rect(dis, blue, [x1, y1, 10, 10]) #crea el snake
    pygame.display.update()   

    clock.tick(30)  
pygame.quit() #termina todo
quit()