import pygame.font
from pygame.sprite import Sprite

'''
@author: nilan
'''

class Button(Sprite):

    def __init__(self, screen, x_pos, y_pos, configuration, msg, width, height, bg_color):

        Sprite.__init__(self)
        self.screen = screen
        self.configuration = configuration

        if(width is None):
            width = configuration.button_width
        if(height is None):
            height = configuration.button_height
        if(bg_color is None):
            bg_color = configuration.button_bg

        # Set dimensions and properties of button
        self.width, self.height = width, height
        self.bg_color = bg_color
        self.x_position, self.y_position = x_pos, y_pos
        self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
        self.font = pygame.font.SysFont(configuration.button_font, configuration.button_font_size)
        self.msg = msg        

        # Button message only needs to be prepped once, not on every blit
        self.prep_msg()

    def prep_msg(self):
        # Turn msg into image that can be rendered
        self.msg_image = self.font.render(self.msg, True, self.configuration.button_text_color)
        # Determine offset to center text on button
        self.msg_x = self.x_position + (self.width - self.msg_image.get_width()) / 2
        self.msg_y = self.y_position + (self.height - self.msg_image.get_height()) / 2

    def blitme(self):
        # Draw blank button, and draw message
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, (self.msg_x, self.msg_y))
