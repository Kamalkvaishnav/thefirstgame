import pygame, random
pygame.init() 
screen = pygame.display.set_mode((800,600))

# Background image
Background = pygame.image.load("Woodbg.jpg")

# name of the game
pygame.display.set_caption("The War")


# Happy man
happy_x = 0
happy_y = 530
happy_x_val = 0
happy_img = pygame.image.load("Happyman.png")


# Angry man .... lists for multiple Angryman
angry_x = []
angry_y = []
angry_x_val = []
angry_img = []
num_of_angry = 5

# multiple angry man appending
for i in range(num_of_angry):
    angry_x.append(random.randint(0,736))
    angry_y.append(random.randint(10,50))
    angry_x_val.append(1)
    angry_img.append(pygame.image.load("Angryman.png"))


# Bullet 
bullet_x = happy_x
bullet_y = 530
bullet_y_val = 1.5
bullet_img = pygame.image.load("Bullet.png")
bullet_state = "invisible"

# collision  (by measuring distance between bullet and angry man)
def collision(angry_x,bullet_x,angry_y,bullet_y):
    distance = ((angry_x-bullet_x)**2 + ((angry_y+30)-bullet_y)**2)**(0.5)
    if distance <= 50:
        return True
    else:
        return False  

# fire and kill
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "visible"
    screen.blit(bullet_img,(x+15,y-40))


# score show 
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
def score(x,y):
    score_text = score_font.render("SCORE : " + str(score_value), True , (0,255,255))
    screen.blit(score_text, (x,y))


# game over text show
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over(x,y):
    over_text = over_font.render("GAME OVER", True , (0,255,255))
    screen.blit(over_text, (x,y))

# main game loop
while True:
    screen.fill((255,255,255))
    screen.blit(Background,(0,10))
    screen.blit(happy_img,(happy_x,happy_y))
    
    # events
    for event in pygame.event.get():
        # exit command
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # movment of happy man
        if event.type==pygame.KEYDOWN:
            #left key
            if event.key == pygame.K_LEFT:
                happy_x_val = -3
            # Right key
            if event.key == pygame.K_RIGHT:
                happy_x_val = 3
            # space for firing bullets
            if event.key == pygame.K_SPACE:
                if bullet_state == "invisible":
                    bullet_x = happy_x
                    fire_bullet(bullet_x,bullet_y)
        # Keys release
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                happy_x_val = 0
            if event.key == pygame.K_RIGHT:
                happy_x_val = 0
        
    
    # baundary for happy
    if happy_x <= 0:
        happy_x = 0
    if happy_x >=736:
        happy_x = 736

    # Angryman movement
    for i in range(num_of_angry):
            angry_x[i] += angry_x_val[i]
            
            # game over
            if angry_y[i] >=430:
                for j in range(num_of_angry):
                    angry_y[j] = 2000
                game_over(200,250)
                score(300,330)
            
            # boundary for angry
            if angry_x[i] <= 0:
                angry_x_val[i] = 1
                angry_y[i] +=10
            elif angry_x[i] >=740:
                angry_x_val[i] = -1 
                angry_y[i] += 10
            
            # make collision
            if collision(angry_x[i], bullet_x, angry_y[i], bullet_y):
                bullet_y = 530
                bullet_state = "invisible"
                angry_x[i] = random.randint(0,736)
                angry_y[i] = random.randint(10,50)
                score_value += 1
            
            screen.blit(angry_img[i],(angry_x[i],angry_y[i]))

    if bullet_state == "visible":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_val
        if bullet_y<=50:
            bullet_state = "invisible"
            bullet_y = 530
    
    
    pygame.draw.line(screen,(255,255,255), (0,460), (800,460), 5)
    angry_x += angry_x_val     
    happy_x += happy_x_val
    score(10,10)
    pygame.display.update()

# I have learned the basic functionality of pygame from a youtube channel, "builtwithpython". I used this as reference. 
# This game is inspired by the space inventors (game).
# For some events, I also use pygame documantation for better understanding. 
        