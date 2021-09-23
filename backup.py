import pygame
import Intro

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("dbs.mp3")
pygame.mixer.music.play(1, 0)
screen = pygame.display.set_mode((1280, 720))


class Player1(object):
    def __init__(self):
        self.image = goku= pygame.image.load("goku/10.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(580,420)
        self.dead=0
    def update(self):
        keys=pygame.key.get_pressed()
        if keys [pygame.K_SPACE]:
            self.image = goku= pygame.image.load("goku/68.png").convert_alpha()
        elif kamehameha.rect.x > 1282:
            self.image = goku= pygame.image.load("goku/10.png").convert_alpha()
        if keys [pygame.K_a]:
            self.image = goku= pygame.image.load("goku/14.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -=10
        elif keys [pygame.K_d]:
            self.image = goku= pygame.image.load("goku/17.png").convert_alpha()
            if self.rect.x < 670:
                self.rect.x += 10
        if keys [pygame.K_w]:
            self.image = goku= pygame.image.load("goku/11.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -=10
        elif keys [pygame.K_s]:
            self.image = goku= pygame.image.load("goku/16.png").convert_alpha()
            if self.rect.y < 670:
                self.rect.y += 10

class Attack1(object):
    def __init__(self):
        self.image = kamehameha = pygame.image.load("goku/kiblast.png").convert_alpha()           
        self.rect = self.image.get_rect()
        self.rect.move_ip(900, 700)
    def update(self):               
        if self.rect.x > 1230:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.rect.x = (goku.rect.x + 20)
                self.rect.y = (goku.rect.y - 15)
        if self.rect.x < 1282:
            self.rect.x += 30

class special1(object):
    def __init__(self):
        self.image = superk = pygame.image.load("goku/superk.png").convert_alpha()           
        self.rect = self.image.get_rect()
        self.rect.move_ip(900, 700)
    def update(self):               
        if self.rect.x > 1230:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_TAB]:
                self.rect.x = (goku.rect.x + 20)
                self.rect.y = (goku.rect.y - 15)
        if self.rect.x < 1282:
            self.rect.x += 22

class gokuHealth(object):
    def __init__(self):
        self.image = gokuHealth = pygame.image.load("gokuHealth.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(18, 4)
    def update(self):
        if gokuHealth.rect.x <= -152:
            goku.dead = 1
        if galick.rect.y >= (goku.rect.y - 56):
            if galick.rect.y <= (goku.rect.y + 62):
                if galick.rect.x >= goku.rect.x:
                    if galick.rect.x <= (goku.rect.x + 23):
                        gokuHealth.rect.x -= 10
                        galick.rect.x = 0
        if seconds > 15:
            if final.rect.y >= (goku.rect.y - 56):
                if final.rect.y <= (goku.rect.y + 62):
                    if final.rect.x >= goku.rect.x:
                        if final.rect.x <= (goku.rect.x + 23):
                            gokuHealth.rect.x -= 30
                            final.rect.x = 0

class Player2(object):
    def __init__(self):
        self.image = vegeta= pygame.image.load("vegeta/7.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(757,420)
        self.dead=0
    def update(self):
        keys=pygame.key.get_pressed()
        if keys [pygame.K_RCTRL]:
            self.image = vegeta= pygame.image.load("vegeta/57.png").convert_alpha()
        elif galick.rect.x < -700:
            self.image = vegeta= pygame.image.load("vegeta/7.png").convert_alpha()
        if keys [pygame.K_LEFT]:
            self.image = vegeta= pygame.image.load("vegeta/12.png").convert_alpha()
            if self.rect.x > 650:
                self.rect.x -=10
        elif keys [pygame.K_RIGHT]:
            self.image = vegeta= pygame.image.load("vegeta/8.png").convert_alpha()
            if self.rect.x < 1230:
                self.rect.x += 10
        if keys [pygame.K_UP]:
            self.im600ge = vegeta= pygame.image.load("vegeta/68.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -=10
        elif keys [pygame.K_DOWN]:
            self.image = vegeta= pygame.image.load("vegeta/10.png").convert_alpha()
            if self.rect.y < 670:
                self.rect.y += 10
class Attack2(object):  
    def __init__(self):
        self.image= galick = pygame.image.load("vegeta/kiblast1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(900,700)
    def update(self):
        if self.rect.x < -75 :
            keys= pygame.key.get_pressed()
            if keys[pygame.K_RCTRL]:
                self.rect.x = (vegeta.rect.x - 50)
                self.rect.y = (vegeta.rect.y - 15)
        if self.rect.x < 1282 :
            self.rect.x -= 30

class special2(object):
    def __init__(self):
        self.image= final = pygame.image.load("vegeta/final.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(900,700)
    def update(self):
        if self.rect.x < 0:
            keys= pygame.key.get_pressed()            
            if keys[pygame.K_RSHIFT]:
                self.rect.x = (vegeta.rect.x - 100)
                self.rect.y = (vegeta.rect.y - 15)
        if self.rect.x< 1282:
            self.rect.x -=22

class vegetaHealth(object):
    def __init__(self):
        self.image = vegetaHealth = pygame.image.load("vegetaHealth.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(1092, 4)
    def update(self):
        if vegetaHealth.rect.x >= 1270:
            vegeta.dead = 1
        if kamehameha.rect.y >= (vegeta.rect.y - 56):
            if kamehameha.rect.y <= (vegeta.rect.y + 62):
                if kamehameha.rect.x >= vegeta.rect.x:
                    if kamehameha.rect.x <= (vegeta.rect.x + 43):
                        vegetaHealth.rect.x += 10
                        kamehameha.rect.x = 1200
        if seconds > 15:
            if superk.rect.y >= (vegeta.rect.y - 56):
                if superk.rect.y <= (vegeta.rect.y + 62):
                    if superk.rect.x >= vegeta.rect.x:
                        if superk.rect.x <= (vegeta.rect.x + 43):
                            vegetaHealth.rect.x += 30
                            superk.rect.x = 1200

if __name__ == '__main__':
    # Variables.
    gameloop = False
    fps = pygame.time.Clock()
    start_ticks=pygame.time.get_ticks()
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    goku = Player1()    
    vegeta = Player2()
    kamehameha = Attack1()
    galick = Attack2()
    bg = pygame.image.load("battle1.jpg").convert()
    gokuHealth= gokuHealth()
    vegetaHealth= vegetaHealth()
    superk = special1()
    final= special2()
    gokubar = pygame.image.load("gokubar.png").convert_alpha()
    vegetabar = pygame.image.load("vegetabar.png").convert_alpha()
    CASE1 = pygame.image.load("win1.png").convert()
    CASE2 = pygame.image.load("win2.png").convert()
    

    while not gameloop:
        goku.update()
        vegeta.update()
        kamehameha.update()
        galick.update()
        gokuHealth.update()
        vegetaHealth.update()
        if seconds > 15:
            superk.update()
            final.update()
        screen.blit(bg, (0, 0))
        screen.blit(goku.image, goku.rect)
        screen.blit(vegeta.image, vegeta.rect)
        screen.blit(kamehameha.image, kamehameha.rect)
        screen.blit(galick.image, galick.rect)
        screen.blit(gokuHealth.image, gokuHealth.rect)
        screen.blit(vegetaHealth.image, vegetaHealth.rect)
        screen.blit(superk.image, superk.rect)
        screen.blit(final.image, final.rect)
        screen.blit(gokubar, (0,0))
        screen.blit(vegetabar, (1088,0))
        if goku.dead == 1:
            screen.blit(CASE1, (530,264))
        if vegeta.dead == 1:
            screen.blit(CASE2, (530,264))
        pygame.display.flip()
        if goku.dead ==1:
            pygame.time.delay(3000)
            gameloop= True
        if vegeta.dead ==1:
            pygame.time.delay(3000)
            gameloop= True
        seconds=(pygame.time.get_ticks()-start_ticks)/1000   
        if seconds>=120:
            gameloop=False
            break
        for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                        gameloop=True
        fps.tick(60)               

pygame.quit()
