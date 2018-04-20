import pygame, pygame.font
from pygame.sprite import Sprite

'''
@author: nilan
'''

class Scoreboard(Sprite):

    def __init__(self, screen, configuration):

        Sprite.__init__(self)
        self.screen = screen
        self.configuration = configuration

        self.initialize_stats()
        
        # Set dimensions and properties of scoreboard
        self.sb_height, self.sb_width = configuration.scoreboard_height, self.screen.get_width()
        self.rect = pygame.Rect(0,0, self.sb_width, self.sb_height)
        self.bg_color=(100,100,100)
        self.text_color = (225,225,225)
        self.font = pygame.font.SysFont('Verdana', 18)

        # Set positions of individual scoring elements on the scoreboard
        self.x_popped_position, self.y_popped_position = 20.0, 10.0
        self.x_timer_position, self.y_timer_position = self.screen.get_width() - 200, 10.0
        self.x_points_position, self.y_points_position = 350, 10.0
        self.x_score_position, self.y_score_position = 150, 10.0
        
        self.timer_value = configuration.timer_value
        self.time_passed = 0

    def initialize_stats(self):
        # Game attributes to track for scoring
        self.balloons_popped = 0
        self.demons_popped = 0
        self.balloons_missed = 0
        self.score = 0
        self.popped_ratio = 1.0
        self.batches_finished = 0

    def prep_scores(self):
        self.popped_string = "Popped: " + str(self.balloons_popped)
        self.popped_image = self.font.render(self.popped_string, True, self.text_color)

        self.score_string = "Score: " + format(self.score, ',d')
        self.score_image = self.font.render(self.score_string, True, self.text_color)

        self.timer_string = "Time left: "
        min_str = self.timer_value // 60
        if(min_str < 10):
            self.timer_string = self.timer_string + "0"
        self.timer_string = self.timer_string + str(min_str)
        self.timer_string = self.timer_string + ":"
        sec_str = self.timer_value % 60
        if(sec_str < 10):
            self.timer_string = self.timer_string + "0"
        self.timer_string = self.timer_string + str(sec_str)
        self.timer_text = self.font.render(self.timer_string, True, self.configuration.button_text_color)

        self.points_string = "Points per Balloon: " + str(self.configuration.points_per_balloon)
        self.points_image = self.font.render(self.points_string, True, self.text_color)

    def update_time(self, time_passed):
        self.time_passed += time_passed
        if(self.time_passed >= 1000):
            self.timer_value = self.timer_value - 1
            self.time_passed = 0

    def blitme(self):
        # Turn individual scoring elements into images that can be drawn
        self.prep_scores()
        # Draw blank scoreboard
        self.screen.fill(self.bg_color, self.rect)
        # Draw individual scoring elements
        self.screen.blit(self.popped_image, (self.x_popped_position, self.y_popped_position))
        self.screen.blit(self.points_image, (self.x_points_position, self.y_points_position))
        self.screen.blit(self.score_image, (self.x_score_position, self.y_score_position))
        self.screen.blit(self.timer_text, (self.x_timer_position, self.y_timer_position))
