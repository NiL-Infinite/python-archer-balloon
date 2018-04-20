import pygame.font
from pygame.sprite import Sprite

'''
@author: nilan
'''

class HomePage(Sprite):

    def __init__(self, screen, configuration):

        Sprite.__init__(self)
        self.screen = screen
        self.configuration = configuration

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont('Verdana', 24)

        # Store the set of instructions
        self.instr_lines = ["Move the mouse to control the archer"]
        self.instr_lines.append("Click to fire the arrow, only when the archer is ready")
        self.instr_lines.append("Pop the balloons with the arrows")
        self.instr_lines.append("Some ballons have demons")
        self.instr_lines.append("Kill the demons too")

        # The instruction message only needs to be prepped once, not on every blit
        self.prep_msg()

    def prep_msg(self):
        y_position = self.configuration.screen_height/2 + self.configuration.button_height
        self.msg_images, self.msg_x, self.msg_y = [], [], []
        for index, line in enumerate(self.instr_lines):
            self.msg_images.append(self.font.render(line, True, self.text_color))
            self.msg_x.append(self.configuration.screen_width/2-self.font.size(line)[0]/2)
            self.msg_y.append(y_position + index*self.font.size(line)[1])

    def blitme(self):
        for msg_x, msg_y, msg_image in zip(self.msg_x, self.msg_y, self.msg_images):
            self.screen.blit(msg_image, (msg_x, msg_y))
