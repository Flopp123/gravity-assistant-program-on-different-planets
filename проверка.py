import pygame  
pygame.init()
f1=pygame.font.Font(None,50)
text1=f1.render('Марс',True,(255,128,0))
f2=pygame.font.Font(None,50)
text2=f2.render('Земля',True,(0,255,0))
f3=pygame.font.Font(None,50)
text3=f3.render('Луна',True,(255,255,255))
f4=pygame.font.Font(None,50)
text4=f4.render('Нептун',True,(0,0,255))
f5=pygame.font.Font(None,50)
text5=f5.render('Юпитер',True,(255,255,255))
bg_image = pygame.image.load('8fa7126910307.5a212a61b74ce.jpg')
bg_image2 = pygame.image.load('unnamed.jpg')
bg_image3 = pygame.image.load('ello-optimized-ed524aa7.jpg')
bg_image4 = pygame.image.load('1625510659_24-kartinkin-com-p-pikselnii-fon-kosmos-krasivie-foni-26.jpg')
bg_image5 = pygame.image.load('wallpapersden.com_city-art-5k_7680x4320.jpg')
bg_images = [bg_image, bg_image2,bg_image3,bg_image4,bg_image5]
bg_index = 0
win = pygame.display.set_mode((1200,770))
pygame.display.set_caption("Slav game")

walkRight = [pygame.image.load('p1_walk01.png'), pygame.image.load('p1_walk02.png'), pygame.image.load('p1_walk03.png'), pygame.image.load('p1_walk04.png'), pygame.image.load('p1_walk05.png'), pygame.image.load('p1_walk06.png'), pygame.image.load('p1_walk07.png'), pygame.image.load('p1_walk08.png'), pygame.image.load('p1_walk09.png')]
walkLeft = [pygame.image.load('p2_walk01.png'), pygame.image.load('p2_walk02.png'), pygame.image.load('p2_walk03.png'), pygame.image.load('p2_walk04.png'), pygame.image.load('p2_walk05.png'), pygame.image.load('p2_walk06.png'), pygame.image.load('p2_walk07.png'), pygame.image.load('p2_walk08.png'), pygame.image.load('p2_walk09.png')]

char = pygame.image.load('p1_front.png')

x = 50
y = 670
width = 40
height = 60
vel = 5
clock = pygame.time.Clock()
isJump = False
jumpCount = 10

left = False
right = False 
walkCount = 0
key_down = 1

def redrawGameWindow():
    global walkCount
    win.blit(bg_images[bg_index], (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
    if bg_index==0:
        win.blit(text1, (10,10))
    if bg_index==1:
        win.blit(text2, (10,10))
    if bg_index==2:
        win.blit(text3, (10,10))
    if bg_index==3:
        win.blit(text4, (10,10))
    if bg_index==4:
        win.blit(text5, (10,10))
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            # pressed_mouse = pygame.mouse.get_pressed()
            # if (event.type==pygame.K_RIGHT or pressed_mouse[2]) and key_down:
            if event.key==pygame.K_0 and key_down:
                bg_index += 1
                key_down = 0

                if bg_index >= len(bg_images):
                    bg_index = 0
        elif event.type == pygame.KEYUP:
            key_down = 1
 

    keys = pygame.key.get_pressed() 
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 1400  - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10 and bg_index==1:
            y -= 0.25 * (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            print('Высота-',670-abs(y),'(см)') 
        elif jumpCount >= -10 and bg_index==0:
            y -= 0.5 * (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            print('Высота-',670-abs(y),'(см)')
        elif jumpCount >= -10 and bg_index==2:
            y -= 1 * (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            print('Высота-',670-abs(y),'(см)')
        elif jumpCount >= -10 and bg_index==3:
            y -= 0.2 * (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            print('Высота-',670-abs(y),'(см)')
        elif jumpCount >= -10 and bg_index==4:
            y -= 0.09 * (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
            print('Высота-',670-abs(y),'(см)')
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow()
pygame.quit()
