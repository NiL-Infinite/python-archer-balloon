'''
@author: nilan
'''

class Config():

    def __init__(self):
        # screen parameters
        self.screen_width, self.screen_height = 800, 600
        self.bg_color = 200, 200, 0
        self.scoreboard_height = 50

        self.button_width, self.button_height = 250, 50
        self.button_bg = (0,163,0)
        self.button_text_color = (235,235,235)
        self.button_font, self.button_font_size = 'Verdana', 24
        self.file=open("highest_score.txt", "r")
        try:
            self.highest_score=int(self.file.read())
        except ValueError:
            self.highest_score=0
        finally:
            self.file.close()


        # game status
        self.game_active = False

        # game over conditions
        self.min_popped_ratio = 0.9
        self.games_played = 0

        self.initialize_game_parameters()

    def initialize_game_parameters(self):
        # game play parameters
        self.balloon_speed = 0.1
        # How quickly the speed of balloons rises
        #  ~1.05 during testing and ~1.01 for actual play
        self.speed_increase_factor = 1.05
        self.points_per_balloon = 10
        self.points_per_demon = 5
        self.negative_points_per_demon = 15
        self.archer_ready_time = 700

        # Number of balloons to release in a spawning:
        self.batch_size = 3

        # Number of batches that must be completed to increment batch_size
        self.batches_needed = 3

        self.timer_value = 20
    
    def set_archer_width(self, width):
        self.archer_width = width

    def check_score(self, score):
        if score > self.highest_score:
            self.highest_score = score
            self.file=open("highest_score.txt", "w+")
            self.file.truncate()
            self.file.write(str(self.highest_score))
            self.file.flush()
            self.file.close()
#             self.file=open("highest_score.txt", "w+")
