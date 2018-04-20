import pygame
from pygame.sprite import Sprite

'''
@author: nilan
'''

class Arrow(Sprite):

    def __init__(self, screen, archer):

        Sprite.__init__(self)
        self.screen = screen
        self.image_tail = pygame.image.load('arrow_tail.png').convert_alpha()
        self.image_head = pygame.image.load('arrow_head.png').convert_alpha()
        self.image_w, self.image_h = self.image_head.get_size()

        self.x_position = archer.image_w
        self.y_position = archer.y_position

        self.arrow_speed = 4

        self.update_rect()

    def blitme(self):
        draw_pos = self.image_tail.get_rect().move(self.x_position-self.image_w/2, self.y_position-self.image_h/2)
        self.screen.blit(self.image_tail, draw_pos)
        draw_pos = self.image_head.get_rect().move(self.x_position+3*self.image_w, self.y_position-self.image_h/2)
        self.screen.blit(self.image_head, draw_pos)

    def update_rect(self):
        self.rect = pygame.Rect(self.x_position+2*self.image_w, self.y_position-self.image_h/2,
                                self.image_w, self.image_h)

    def update(self):
        self.x_position += self.arrow_speed
        self.update_rect()
