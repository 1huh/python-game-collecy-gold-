import pygame
import random

pygame.init()

#dimensions 
screen_x = 900 
screen_y = 500

#window config
game_window = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("Gold Cave")
game_running = True

#tick
clock = pygame.time.Clock()

#colors
red = (252, 19, 3)
purple = (96, 50, 168)
white = (255, 255, 255)
green = (0, 144, 42)
yellow = (255,215,0)
blue = (52, 97, 235)
black = (0, 0, 0)
pink = (245, 66, 206)
l_blue = (66, 245, 236)
brown = (128,0,0)
magenta = (171, 7, 163)
orange = (255, 2,0)
#player_stuff
p_speed = 1
p_x = screen_x/2
p_y = screen_y/2
p_block = 20
p_col = green
score = 0
#gold
gold_num = 1
gold = []
g_block = 15
g_col = yellow
g_x = random.randint(100, 800)
g_y = random.randint(50,450)
#rocks
rock_num = 4
rock_l = []
rock_t = []
r_block = 15
r_col = brown
rx_l = 0
ry_l = random.randint(50,490)
rx_t = random.randint(50, 890)
ry_t = 0
r_speed = 4

#lives
num_lives = 3

#rectabgle surfaces
player = pygame.Rect(p_x, p_y, p_block,p_block)
for i in range (gold_num): 
    gold.append(pygame.Rect(g_x,g_y,g_block,g_block))
for i in range (rock_num): 
    rock_l.append(pygame.Rect(rx_l,ry_l,r_block, r_block ))
for i in range(rock_num): 
    rock_t.append(pygame.Rect(rx_t, ry_t,r_block, r_block ))
#functions
#text function
def txt(txt,m, x, y, c, s):
    font = pygame.font.Font('freesansbold.ttf', s)
    dText = font.render(str(txt) + str(m), True, (c))
    game_window.blit(dText, (x, y))
#movement function
def move(l):
    if str(l) == "a" and player.x > 0:
        for i in range(10): 
            player.x -= p_speed
    if str(l) == "w" and player.y > 0:
        for i in range(10): 
            player.y -= p_speed
    if str(l) == "s" and player.y < screen_y - p_block:
        for i in range(10): 
            player.y += p_speed
    if str(l) == "d" and player.x < screen_x - p_block:
        for i in range(10): 
            player.x += p_speed

#booleans 
gameOver = False
winner = False
pregame = True
#background images
bground = pygame.image.load("minent.png")
bground2 = pygame.image.load("cave.png")
while game_running: 
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_running = False

#gold collection
    for i in range(gold_num): 
        if player.colliderect(gold[i]): 
            gold[i].x = random.randint(100,800) + r_speed
            gold[i].y = random.randint(50,450)  
            if gold[i].x == 700: 
                gold[i].x - r_speed
            score += 1 
                    
#adding the pregame picture
    game_window.blit(bground,(0,0))

#pregame screen
    keys = pygame.key.get_pressed()
    if pregame == True: 
        txt("GOLD CAVE","" ,screen_x/2.859, screen_y/15, yellow, 50)
        txt("PRESS SPACE TO START", '', screen_x/2.8, screen_y/ 1.2, magenta, 24)
        txt("CONTROLS: HOLD", '', screen_x/15, screen_y/4.5, brown, 30 )
        txt("W = UP, S = DOWN", '', screen_x/15, screen_y/3, blue, 15)
        txt("A = LEFT, D = RIGHT", '', screen_x/15, screen_y/2.6, blue, 15 )
        txt("Avoid the rocks! ", '', screen_x/15, screen_y/2, red, 25)
        txt("Collect 25 gold to win!", '', screen_x/15, screen_y/1.8, red, 25)
        if keys[pygame.K_SPACE]: 
            pregame = False
            winner = False
            score = 0
#movement#score keeping #drawing player
#generating gold and rocks

    if pregame == False and gameOver == False:
        game_window.blit(bground2,(0,0))
        if keys[pygame.K_w]:
            move("w")     
        elif keys[pygame.K_s]: 
            move("s")
        elif keys[pygame.K_a]: 
            move("a")
        elif keys[pygame.K_d]:
            move("d")
        txt("LIVES: ",num_lives, screen_x/ 1.5, screen_y/15, yellow, 32)
        txt("SCORE: ",score, screen_x/3.8, screen_y/15, yellow, 32 )
        pygame.draw.rect(game_window, p_col, player)
        for i in range(gold_num): 
            pygame.draw.rect(game_window, g_col, gold[i])
        for i in range(rock_num): 
            pygame.draw.rect(game_window,r_col, rock_l[i])
            pygame.draw.rect( game_window, r_col, rock_t[i])

#losing the game 
    if gameOver == True:
        game_window.fill(white)
        txt("GAMEOVER!",'',screen_x/2.859, screen_y/15, yellow, 50)
        txt("FINAL SCORE: ",score,screen_x/7, screen_y/5, l_blue, 25)
        txt("PRESS SPACE TO PLAY AGAIN",'', screen_x/2, screen_y/5, blue, 25)
        txt("PRESS T TO QUIT",'', screen_x/2.8, screen_y/2, red, 25)
        if keys[pygame.K_SPACE]: 
            gameOver = False
            score = 0
            num_lives = 3
        if keys[pygame.K_t]: 
            game_running = False

    #winning the thing
    if score == 20:
        game_window.fill(white)
        txt("YOU WON!",'',screen_x/2.859, screen_y/15, yellow, 50)
        txt("PRESS SPACE TO PLAY AGAIN",'', screen_x/3, screen_y/5, blue, 25)
        txt("PRESS T TO QUIT",'', screen_x/2.8, screen_y/2, red, 25)
        if keys[pygame.K_t]: 
            game_running = False
        if keys[pygame.K_SPACE]: 
            gameOver = False
            score = 0
            num_lives = 3
#starting the game 
    if pregame == False: 
        for i in range(rock_num): 
            rock_l[i].x += r_speed
            rock_t[i].y += r_speed
            if rock_l[i].x == 800:
                rock_l[i].y = random.randint(50,400) + r_speed
                rock_l[i].x = 12
            if rock_t[i].y == 400: 
                rock_t[i].x = random.randint(50,890) + r_speed
                rock_t[i].y = 12
    for i in range(rock_num):
        if player.colliderect(rock_l[i]) or player.colliderect(rock_t[i]):
            num_lives -= 1
            rock_l[i].y = random.randint(50,400)
            rock_l[i].x = 12
            rock_t[i].x = random.randint(50, 890)
            rock_t[i].y = 12
            if num_lives == 0:   
                gameOver = True
                rock_l[i].y = random.randint(50,400)
                rock_l[i].x = 12
                rock_t[i].x = random.randint(50, 890)
                rock_t[i].y = 12
                player.x = screen_x/2
                player.y = screen_y/2


    pygame.display.update()
pygame.quit()
