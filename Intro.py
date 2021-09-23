import pygame

FPS = 60
BGCOLOR = pygame.image.load('cover2.png')


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Project")
        self.running = True

    def show_start_screen(self):
        # game splash/start screen  
        self.screen.blit(BGCOLOR, (0, 0))
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False

g = Game()
g.show_start_screen()

pygame.quit()
