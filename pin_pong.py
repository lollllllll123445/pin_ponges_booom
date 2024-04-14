#for smile face
from pygame import*
window = display.set_mode((700 , 500))
display.set_caption("пинапонгус")

backround = transform.scale(image.load("джумаджи.jpg"),(700,500))

speed_x = 2
speed_y = 2
#класс GameSpirite
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    
    def reset(self):
        window.blit(self.image, (self.rect.x , self.rect.y))
    
    def move(self):
        global speed_x
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y >= 460 or self.rect.y <= 0:
            speed_y *= -1
        '''if self.rect.x >= 650 or self.rect.y <= 0:
            speed_x *= -1'''
        if platform1.rect.colliderect(self.rect):
            speed_x *= -1
        if platform2.rect.colliderect(self.rect):
            speed_x *= -1

#наследник класса PLAYER
class player(GameSprite):
    def update(self):
        keys_pressed =  key.get_pressed()

        if keys_pressed[K_w] and self.rect.y >5:
            self.rect.y -= 5  
        
        if keys_pressed[K_s] and self.rect.y <390:
            self.rect.y += 5
    
    def update1(self):
        keys_pressed =  key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y >5:
            self.rect.y -= 5   
        
        if keys_pressed[K_DOWN] and self.rect.y <390:
            self.rect.y += 5




platform1 = player("platform.png",1,250,230)
platform2 = player("platform.png",670,250,230)
platform1.image = transform.scale(platform1.image,(25,100))
platform2.image = transform.scale(platform2.image,(25,100))
platform1.rect = platform1.image.get_rect()
platform2.rect = platform2.image.get_rect()
platform2.rect.x = 670
ball = GameSprite("джужу.png",50,150,413)
ball.image = transform.scale(ball.image,(50,50))
game = True
while game:
     
    window.blit(backround,(0,0))
    #ресеты,апдейты,дравы
    platform1.update()
    platform2.update1()
    platform1.reset()
    platform2.reset()
    ball.reset()
    ball.move()
    for e in event.get():
        if e.type == QUIT:
            game = False
                
                    
               
    
    display.update()