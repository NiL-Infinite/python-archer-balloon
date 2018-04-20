import pygame
from Config import Config
from Scoreboard import Scoreboard
from Button import Button
from GamePlay import GamePlay
from HomePage import HomePage
from Archer import Archer

'''
@author: nilan
'''

def run_game():
    # Get access to our game configuration
    configuration = Config()

    # initialize game
    pygame.init()
    screen = pygame.display.set_mode((configuration.screen_width, configuration.screen_height), 0, 32)
    clock = pygame.time.Clock()
    scoreboard = Scoreboard(screen, configuration)
    play_button = Button(screen, configuration.screen_width/2-configuration.button_width/2,
                            configuration.screen_height/2-configuration.button_height/2, configuration, "Play", None, None, None)
    game_over_button = Button(screen, play_button.x_position, play_button.y_position-3*configuration.button_height,
                              configuration, "Game Over!", None, None, (160,0,0))
    score_button = Button(screen, play_button.x_position, play_button.y_position-2*configuration.button_height,
                              configuration, "Score:", None, None, (255,69,0))
    highest_score_button = Button(screen, play_button.x_position, play_button.y_position-configuration.button_height,
                              configuration, "Highest Score:" + str(configuration.highest_score), None, None, (255,69,0))
    heading_button = Button(screen, 0, 0,
                              configuration, "Bows and Balloons", 800, None, (160,0,160))
    home_page = HomePage(screen, configuration)

    balloons = []
    demons = []
    arrows = []

    # Create our dagger
    # sword = Sword(screen, configuration.scoreboard_height)
    archer = Archer(screen, configuration.scoreboard_height)

    configuration.set_archer_width(archer.image_w)

    # Create our game game_play, with access to appropriate game parameters:
    game_play = GamePlay(screen, configuration, scoreboard, balloons, demons, archer, arrows)

    # main event loop
    while True:
        # Advance our game clock, get the current mouse position, and check for new events
        time_passed = clock.tick(50)
        mouse_x, mouse_y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
        game_play.check_events(play_button, mouse_x, mouse_y)

        # Redraw the empty screen before redrawing any game objects
        screen.fill(configuration.bg_color)

        if configuration.game_active:
            # Update the sword's position and check for popped or disappeared balloons
            game_play.update_archer(mouse_x, mouse_y, time_passed)
            game_play.check_balloons(time_passed)
            game_play.check_demons()
            game_play.check_arrows()
            scoreboard.update_time(time_passed)

            # If all balloons have disappeared, either through popping or rising,
            #  release a new batch of balloons.
            if len(balloons) == 0:
                # If we are not just starting a game, increase the balloon speed and points per balloon,
                #  and increment batches_finished
                if scoreboard.balloons_popped > 0:
                    #  Increase the balloon speed, and other factors, for each new batch of balloons.
                    configuration.balloon_speed *= configuration.speed_increase_factor
                    configuration.points_per_balloon = int(round(configuration.points_per_balloon * configuration.speed_increase_factor))
                    scoreboard.batches_finished += 1
                # If player has completed required batches, increase batch_size
                if scoreboard.batches_finished % configuration.batches_needed == 0 and scoreboard.batches_finished > 0:
                    configuration.batch_size += 1
                game_play.release_batch()
            scoreboard.blitme()
        else:
            # Game is not active, so...
            #  Show play button
            score_button.msg = "Score: " + str(scoreboard.score)
            score_button.prep_msg()
            play_button.blitme()
            #  Show instructions for first few games.
            #  if configuration.games_played < 3:
            home_page.blitme()
            #  If a game has just ended, show Game Over button
            if configuration.games_played > 0:
                game_over_button.blitme()
                score_button.blitme()
                configuration.check_score(scoreboard.score)
                highest_score_button.msg = "Highest Score: " + str(configuration.highest_score)
                highest_score_button.prep_msg()
            highest_score_button.blitme()
            heading_button.blitme()
        
        # Display updated scoreboard

        # Show the redrawn screen
        pygame.display.flip()

run_game()
