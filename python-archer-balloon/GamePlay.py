import pygame, sys
from Balloon import Balloon
from Arrow import Arrow

'''
@author: nilan
'''

class GamePlay():

    def __init__(self, screen, configuration, scoreboard, balloons, demons, archer, arrows):
        self.screen = screen
        self.configuration = configuration
        self.scoreboard = scoreboard
        self.balloons = balloons
        self.demons = demons
        self.archer = archer
        self.arrows = arrows
        self.archer_time = 0

    def release_batch(self):
        for x in range(0, self.configuration.batch_size):
            self.spawn_balloon()
        print(self.configuration.batch_size)

    def check_balloons(self, time_passed):
        # Find any balloons that have been popped,
        #  or have disappeared off the top of the screen
        for balloon in self.balloons:
            balloon.update(time_passed)

            arrow = self.check_arrow_balloon_collision(balloon)
            if arrow is not None:
                self.pop_balloon(balloon, arrow)
                continue

            if balloon.y_position < -balloon.image_h/2 + self.configuration.scoreboard_height:
                self.miss_balloon(balloon)
                self.spawn_balloon()
                continue

            balloon.blitme()

        if self.scoreboard.timer_value <= 0:
                # Set game_active to false, empty the list of balloons, and increment games_played
                self.configuration.game_active = False
                self.configuration.games_played += 1

    def check_demons(self):
        # Find any balloons that have been popped,
        #  or have disappeared off the top of the screen
        for demon in self.demons:
            demon.walk()
            demon.blitme()
            if self.check_arrow_demon_collision(demon):
                self.pop_demon(demon, 1)
                continue
            if self.check_archer_demon_collision(demon):
                self.archer.update_status(3)
                self.pop_demon(demon, -1)
                continue
                

    def check_arrows(self):
        for arrow in self.arrows:
            arrow.update()
            if arrow.x_position > self.screen.get_width():
                self.miss_arrow(arrow)
            arrow.blitme()

    def check_arrow_balloon_collision(self, currentBalloon):
        for arrow in self.arrows:
            if currentBalloon.rect.colliderect(arrow.rect):
                return arrow
        return None

    def check_arrow_demon_collision(self, demon):
        for arrow in self.arrows:
            if demon.rect.colliderect(arrow.rect):
                return True
        return False

    def check_archer_demon_collision(self, demon):
        if demon.rect.colliderect(self.archer.rect):
            return True
        return False

    def update_archer(self, mouse_x, mouse_y, time_passed):
        # Update the sword's position, and draw the sword on the screen
        if(self.archer_time > self.configuration.archer_ready_time):
            self.archer.auto_update_archer()
            self.archer_time = 0
        else:
            self.archer_time += time_passed
        self.archer.y_position = mouse_y
        self.archer.update_rect()
        self.archer.blitme()

    def miss_balloon(self, balloon):
        self.scoreboard.balloons_missed += 1
        self.balloons.remove(balloon)

    def miss_arrow(self, arrow):
        self.arrows.remove(arrow)

    def pop_balloon(self, balloon, arrow):
        self.scoreboard.balloons_popped += 1
        self.scoreboard.score += self.configuration.points_per_balloon
        if(balloon.demon is not None):
            balloon.demon.load_image('walking_demon_1.gif')
            balloon.demon.updateY(arrow.y_position + balloon.demon.image_h + 5)
            self.demons.append(balloon.demon)
        self.balloons.remove(balloon)

    def pop_demon(self, demon, points):
        if(points > 0):
            self.scoreboard.demons_popped += 1
            self.scoreboard.score += self.configuration.points_per_demon
        else:
            self.scoreboard.score -= self.configuration.negative_points_per_demon
            if self.scoreboard.score < 0:
                self.scoreboard.score = 0
        self.demons.remove(demon)

    def spawn_balloon(self):
        self.balloons.append(Balloon(self.screen, self.configuration))

    def check_events(self, play_button, mouse_x, mouse_y):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.archer.status == 0:
                    arrow = Arrow(self.screen, self.archer)
                    self.arrows.append(arrow)
                    self.archer.update_status(1)
                if play_button.rect.collidepoint(mouse_x, mouse_y) and not self.configuration.game_active:
                    # Play button has been pressed.  Empty list of balloons,
                    #  initialize scoreboard and game parameters, and make game active.
                    del self.balloons[:]
                    del self.arrows[:]
                    del self.demons[:]
                    self.scoreboard.initialize_stats()
                    self.configuration.initialize_game_parameters()
                    self.configuration.game_active = True
                    self.scoreboard.timer_value = self.configuration.timer_value
                    self.archer.update_status(0)
#             if event.type == pygame.MOUSEBUTTONUP:
#                 self.sword.grabbed = False
