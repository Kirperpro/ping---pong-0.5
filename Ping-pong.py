from pygame import *

font.init()
font2 = font.SysFont('Arial', 36) #шрифт

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 170))                
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):     
        window.blit(self.image, (self.rect.x, self.rect.y))

ochki1 = 0
ochki2 = 0        

class Player1(GameSprite):
    def update(self):
        global ochki1
        if self.rect.x > win_width:
            ochki1 += 1
        keys_passed = key.get_pressed()
        if keys_passed [K_w] and y2 < 395:
            self.rect.y-=self.speed
        if keys_passed [K_s] and y2 < 395:
            self.rect.y+=self.speed  

class Player2(GameSprite):
    def update(self):
        global ochki2
        if self.rect.x < 0:
            ochki2 += 1
        keys_passed = key.get_pressed()
        if keys_passed [K_UP] and y2 < 395:
            self.rect.y-=self.speed
        if keys_passed [K_DOWN] and y2 < 395:
            self.rect.y+=self.speed  

player1 = Player1('igrok1n.png', 15, 130, 6)
player2 = Player2('igrok2n.png', 635, 130, 6)

win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Жоски пинг-понг от Мистера Биста!!!')
Background = transform.scale(image.load('fon.png'),(700, 500))

mixer.init()
mixer.music.load('fonmuz.ogg')
mixer.music.play()

x1 = 100
y1 = 100
x2 = 200
y2 = 100

game = True

cock = time.Clock() #clock
FPS = 60

while game:
    window.blit(Background, (0, 0))
    for e in event.get():
            if e.type == QUIT:
                game = False

    if ochki1 >= 10:
        win = font2.render('Победа игрока 1!', True, (0,255,0))
        window.blit(win,(250,250))
        game = False

    if ochki2 >= 10:
        win = font2.render('Победа игрока 2!', True, (0,255,0))
        window.blit(win,(250,250))
        game = False

    player1.reset()
    player2.reset()
    player1.update()
    player2.update()
    display.update()
    cock.tick(FPS) 