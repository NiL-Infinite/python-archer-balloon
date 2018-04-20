import pygame
from pygame.sprite import Sprite

'''
@author: nilan
'''

class Archer(object):
    def __init__(self, screen, scoreboard_height):

        Sprite.__init__(self)
        self.screen = screen
        self.arrowReady = pygame.image.load('arrow_ready.png').convert_alpha()
        self.arrowFiredImage = pygame.image.load('arrow_fired.png').convert_alpha()
        self.noArrowImage = pygame.image.load('no_arrow.png').convert_alpha()
        self.archerDemonHit = pygame.image.load('archer_demon_hit.png').convert_alpha()
        
        self.image = self.arrowReady
        self.image_w, self.image_h = self.image.get_size()

        self.x_position = self.image_w/2
        self.y_position = self.image_h/2 + scoreboard_height

        self.status = -1 # -1:game_paused, 0:arrow_ready, 1:arrow_fired, 2:no_Arrow
        self.ticks = 0

        self.update_rect()

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position-self.image_w/2, self.y_position-self.image_h/2)
        self.screen.blit(self.image, draw_pos)

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position-self.image_w/2, self.y_position-self.image_h/2, self.image_w, self.image_h)
#         print("x:" + str(self.x_position) + "y:" + str(self.y_position))

    def update_status(self, status):
        self.status = status
        if (status == 0):
            self.image = self.arrowReady
        elif (status == 1):
            self.image = self.arrowFiredImage
        elif (status == 2):
            self.image = self.noArrowImage
        elif (status == 3):
            self.image = self.archerDemonHit
        self.blitme()

    def auto_update_archer(self):
        if self.status == 1:
            self.status = 2
        elif self.status == 2:
            self.status = 0
        elif self.status == 3:
            self.status = 2
        self.update_status(self.status)