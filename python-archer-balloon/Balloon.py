import pygame
from pygame.sprite import Sprite
from random import randint, uniform
from Demon import Demon

'''
@author: nilan
'''

class Balloon(Sprite):

    def __init__(self, screen, configuration):

        Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load('balloon.png').convert_alpha()
        self.image_w, self.image_h = self.image.get_size()
        self.speed = uniform(0.75,1.25)*configuration.balloon_speed

        self.x_position = randint(self.image_w/2 + configuration.archer_width*2, self.screen.get_width()-self.image_w/2)
        max_offset = min(configuration.batch_size*self.image_h, self.screen.get_height())
        self.y_position = self.screen.get_height() + self.image_h/2 + randint(0, max_offset)
        self.demon = None
        if(randint(0, 100) % 2 == 1):
            self.demon = Demon(screen, self.x_position, self.y_position, self.image_w, self.image_h)

        self.update_rect()

    def update(self, time_passed):
        self.y_position -= self.speed * time_passed
        if(self.demon is not None):
            self.demon.update(self.speed * time_passed)
        self.update_rect()

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position-self.image_w/2, self.y_position-self.image_h/2)
        self.screen.blit(self.image, draw_pos)
        if(self.demon is not None):
            self.demon.blitme()

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position-self.image_w/2, self.y_position-self.image_h/2,
                                self.image_w, self.image_h)
