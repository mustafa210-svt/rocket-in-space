import pygame

#screen size
WIDTH = 600
HEIGHT = 600
TITLE = "Rocket in space"

#setting up the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
#variables
run = True 
space = pygame.image.load("space background.png")
rocket = pygame.image.load("rocket.png")
y_cord =  300
x_cord = 300
#while loop

#events
while run == True:
    
    #space background
    screen.blit(space,(0,0))

    #rocket 
    screen.blit(rocket,(x_cord,y_cord))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           run = False
        if event.type == pygame.KEYDOWN:#only works if you spam click the keys
            #W key
            if event.key == pygame.K_w:
                y_cord = y_cord - 5
            #S key
            if event.key == pygame.K_s:
                y_cord = y_cord + 5
            #D key
            if event.key == pygame.K_d:
                x_cord = x_cord + 5
            #A key
            if event.key == pygame.K_a:
                x_cord = x_cord - 5
             
    key_pressed = pygame.key.get_pressed()# Now you have to hold the keys for it to move
    #W key
    if key_pressed[pygame.K_w]:
        y_cord = y_cord - 5
    #S key
    if key_pressed[pygame.K_s]:
        y_cord = y_cord + 5
    #D key
    if key_pressed[pygame.K_d]:
        x_cord = x_cord + 5
    #A key
    if key_pressed[pygame.K_a]:
        x_cord = x_cord - 5
     
    #bounderies for screen
    #x cord
    if x_cord >= 450:
        x_cord = 450
    if x_cord <= 0:
        x_cord = 0
    #y cord
    if y_cord >=400:
        y_cord = 400
    if y_cord <= 0:
        y_cord = 0


           
    
        
    pygame.display.update()