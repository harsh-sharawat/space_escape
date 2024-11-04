import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((1000,800))

#tittle and icon

pygame.display.set_caption("space_escape")
# icon=pygame.image.load('planet.png')
# pygame.display.set_icon(icon)
px=470
py=700
cx,cy=0,0

bx,by,cby=0,0,0

#background image
back=pygame.image.load('back.png').convert()
background=pygame.transform.scale(back,(940,740))


#main player 
p_img=pygame.image.load('ship.png')

def player(px=470,py=700) :
    screen.blit(p_img,(px,py))




#bullet formation

bullet_img=pygame.image.load('bullet.png')
bullet_image = pygame.transform.scale(bullet_img ,(40,30))
bullet_state=False
def bullet(bx,by):
    
    screen.blit(bullet_image,(bx,by))



#rock formation

rock_state=False
rock_size=0
rock_count=0
rock_img=pygame.image.load('rock.png')

def rock(rx,ry,rock_size):
    

    
   
    rock_scale=pygame.transform.scale(rock_img,(rock_size,rock_size))
    screen.blit(rock_scale,(rx,ry))
    


def iscollision(bx,by,rx,ry,rock_size):
   

    rock_center_x = rx + rock_size / 2
    rock_center_y = ry + rock_size / 2
    
   
    bullet_center_x = bx + bullet_image.get_width() / 2
    bullet_center_y = by + bullet_image.get_height() / 2
    
    distance = (bullet_center_x - rock_center_x) ** 2 + (bullet_center_y - rock_center_y) ** 2
    
    threshold = (rock_size / 2) ** 2  
    
    return distance < threshold


#gamer over logic:
def gameover(px,py,rx,ry,rock_size):
   

    rock_center_x = rx + rock_size / 2
    rock_center_y = ry + rock_size / 2
    
   
    player_center_x = px + p_img.get_width() / 2
    player_center_y = py + p_img.get_height() / 2
    
    distance = (player_center_x - rock_center_x) ** 2 + (player_center_y - rock_center_y) ** 2
    
    threshold = (rock_size / 2+(p_img.get_width()+p_img.get_height())/4) ** 2  
    
    return distance < threshold



score=0
font=pygame.font.Font('freesansbold.ttf',30)
def show_score():
    s=font.render("SCORE : "+str(score),True,(255,0,0))
    l=font.render('LEVEL : '+str((score//10)+1),True,(255,100,0))
    screen.blit(l,(790,100))
    screen.blit(s,(790,40))

running = True

game_state=False
while running: 
    screen.blit(background,(30,20))

    pygame.draw.rect(screen, (0,0,0),(30,20,740,760),4)

    pygame.draw.rect(screen, (0,0,0),(780,20,190,760),4)

    
   
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False

        if event.type== pygame.KEYDOWN:
            if not game_state:

                if event.key== pygame.K_LEFT:
                    cx-=4
                    
                if event.key == pygame.K_RIGHT:
                    cx+=4
                if event.key == pygame.K_UP:
                    cy-=4
                if event.key == pygame.K_DOWN:
                    cy+=4

                if event.key == pygame.K_SPACE:
                    if not bullet_state:
                        bx=px+12
                        by=py-20
                        bullet_state=True

        if event.type == pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                cx=0
                cy=0


    

    if game_state:
        over_font = pygame.font.Font('freesansbold.ttf', 50)
        game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))
        score_text = over_font.render(f"SCORE: {score}", True, (0, 255, 0))
        restart_font = pygame.font.Font('freesansbold.ttf', 20)
        restart_text = restart_font.render('Press SPACE to restart', True, (100, 100, 255))
        screen.blit(game_over_text,(200,400))
        screen.blit(score_text,(200,200))
        screen.blit(restart_text,(200,600))
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    score=0
                    px=470
                    py=700
                    rock_state=False
                    bullet_state=False
                    cx,cy=0,0

                    bx,by,cby=0,0,0
                    game_state=False
        pygame.display.update()

        continue
    px+=cx
    py+=cy
    px=max(35,px)
    px=min(700,px)
    py=max(40,py)
    py=min(700,py)

    
    player(px,py)

    if(bullet_state):
        bullet(bx,by)
        by-=5
        if(by<=30):
            bullet_state=False
    

    if not rock_state:
        rock_state=True
        rock_count+=1
        rx=random.choice([i for i in range(30,670,1)])
        ry=20
        rock_size = random.choice([i for i in range(40,100,10)])
    if rock_state:
        rock(rx,ry,rock_size)
      #  pygame.draw.rect(screen, (200,0,0),(rx,ry,rock_size,rock_size),2)
        ry+=(1 + (score*0.05))
        
        if(ry>=670):
            rock_state=False
    

    if(gameover(px,py,rx,ry,rock_size)):
       game_state=True

    



    if iscollision(bx,by,rx,ry,rock_size):
        bullet_state=False
        rock_state=False
        score+=1

    show_score()
    



    pygame.display.update()
    