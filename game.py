import pygame
import random
pygame.init()

height_win = 900
width_win = 1400

Green = (15,190,10)
red = (230,20,10)

window = pygame.display.set_mode((width_win, height_win))
clock = pygame.time.Clock()

text_lose = pygame.font.SysFont(None, 50).render("Вы проиграли", True, Green)
text_lose_2 = pygame.font.SysFont(None, 50).render("Для перезапуска нажмите пробел", True, Green)
text_win = pygame.font.SysFont(None, 50).render("Вы выиграли, УРА!!!!!!", True, red)

background = pygame.transform.scale(pygame.image.load('background.jpg'), (width_win, height_win))
player_img = pygame.transform.scale(pygame.image.load('platform.png'), (180, 80))
enemy_img = pygame.transform.scale(pygame.image.load('star.png'), (55, 55))
ball_img = pygame.transform.scale(pygame.image.load('ball.png'), (55, 55))
enemies_rect = []
x = 50
y = 50

for i in range(1):
    for j in range(1):
        tm_rect = enemy_img.get_rect()
        tm_rect.x = x
        tm_rect.y = y
        enemies_rect.append(tm_rect)
        x+= 150
    x = 50
    y += 100

player_rect = player_img.get_rect()
player_rect.x = 600
player_rect.y = 800
ball_rect = ball_img.get_rect()
ball_rect.x = 650
ball_rect.y = 550
def game_loop():
    speed_x = 3
    speed_y = -3
    flag_win = False
    flag_lose = False
    while True:
        window.blit(background,(0,0))
        window.blit(player_img, player_rect)
        window.blit(ball_img, ball_rect)
        
        if flag_win:
            window.blit(text_win, (500,400))
            break
        if flag_lose:
            window.blit(text_lose, (700, 400))
            window.blit(text_lose_2, (700, 500))
            pygame.display.update()
            return 0 
        
        for i in enemies_rect:
            window.blit(enemy_img, i)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
        keys = pygame.key.get_pressed()
        if keys [pygame.K_d]:
            player_rect.x += 5                                                                          
        if keys [pygame.K_a]:
            player_rect.x -= 5
        
        if ball_rect.right >= width_win:
            speed_x *= -1
            
        if ball_rect.top <= 0 :
            speed_y *= -1
        
        if ball_rect.x <= 0:
            speed_x *= -1
            
        if ball_rect.y >= height_win:
            flag_lose = True
        
        if not flag_lose:  
            for i in enemies_rect:
                if ball_rect.colliderect(i):
                    speed_y *= -1
                    enemies_rect.remove(i)

      
                    if random.random() < 0.5:  # Вероятность 50%
                        speed_x *= random.uniform(0.5, 1.5)  # Ускорение в случае попадания
                        speed_y *= random.uniform(0.5, 1.5)
                    else:
                        speed_x *= random.uniform(0.5, 1.5)  # Замедление в другом случае
                        speed_y *= random.uniform(0.5, 1.5)
        
        if player_rect.colliderect(ball_rect):
            if ball_rect.bottom >= player_rect.y + speed_y:
                if player_rect.center[0] > ball_rect.x:
                    ball_rect.x -= abs(speed_x) * 2
                else:
                    ball_rect.x += abs(speed_x) * 2
                speed_x *= -1
            speed_y *= -1
            
        
        for i in enemies_rect:
            if ball_rect.colliderect(i):
                speed_y *= -1
                enemies_rect.remove(i)
        
    
        ball_rect.x += speed_x
        ball_rect.y += speed_y
        
        if len(enemies_rect) == 0:
            flag_win = True
            
            
        clock.tick(90)
        pygame.display.update()
            
flag_play = False
while True:
    if flag_play:
        flag_play = game_loop()    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flag_play = True

    
    



        
 

