import pygame
from pygame.sprite import Sprite

'''
@author: nilan
'''

class Demon(Sprite):

    def __init__(self, screen, x_position, y_position, width, height):

        Sprite.__init__(self)
        self.screen = screen
        self.load_image('demon.png')
        self.image_w, self.image_h = self.image.get_size()

        self.x_position = x_position #+ (width - self.image_w)//2
        self.y_position = y_position #+ (height - self.image_h)//2
        self.speed = 3

        self.update_rect()

    def load_image(self, path):
        self.image = pygame.image.load(path).convert_alpha()
        self.image_w, self.image_h = self.image.get_size()

    def blitme(self):
        draw_pos = self.image.get_rect().move(self.x_position - self.image_w/2, self.y_position - self.image_h/2)
        self.screen.blit(self.image, draw_pos)

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position - self.image_w/2, self.y_position, self.image_w, self.image_h - self.image_h/2)

    def update(self, y_offset):
        self.y_position -= y_offset
        self.update_rect()

    def updateY(self, y_position):
        self.y_position = y_position
        self.update_rect()
    
    def walk(self):
        self.x_position -= self.speed
        self.update_rect()