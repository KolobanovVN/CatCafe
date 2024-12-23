import pygame

from src.game_server import GameServer
from src.resource import RESOURCE as RSC
from src.ui.view_game import ViewGame

class Application:

    def __init__(self):
        pygame.init()
        self.size = (self.width, self.height) = (RSC['width'], RSC['height'])
        self.display = pygame.display.set_mode(self.size)
        pygame.display.set_caption(RSC['title'])
        try:
            icon_img = pygame.image.load("img/game_icon.png")
            pygame.display.set_icon(icon_img)
        except FileNotFoundError:
            pass
        self.vgame = ViewGame()

    def run(self):
        clock = pygame.time.Clock()
        running = True
        self.display.fill((255, 255, 170), (0, 0, self.width, self.height))
        pygame.display.update()
        while running:
            self.vgame.model_update()
            self.vgame.redraw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    running = False
                self.vgame.event_processing(event)
            clock.tick(RSC["FPS"])

    def connect_with_game(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.run()
