import turtle

OUTPUT_SPACE_COORDS = True

class Gameboard():
    # declare window
    win = turtle.Screen()
    # declare turtle
    t = turtle.Turtle()
    # declare default board data & configs
    game_board_data = {}
    configs = {}

    # list to hold the players

    def __init__(self, game_board_data, configs):
        self.win.screensize(configs["game_win_size_x"], configs["game_win_size_y"])
        self.win.bgcolor(configs["game_win_bg_color"])
        self.game_board_data = game_board_data
        self.configs = configs
        self.draw_game_board_stops()

    def draw_game_board_stops(self):
        self.t.speed(0)
        self.t.up()
        self.t.pensize(5)
        self.t.left(90)  # make the turtle face up
        self.t.shape("circle")
        self.t.color('#AAA') # TODO is this necessary?

        # draw the background road
        self.t.goto(self.configs["road_start_pos_x"], self.configs["road_start_pos_y"])
        self.t.down()
        self.t.goto(self.configs["road_end_pos_x"], self.configs["road_end_pos_y"])
        self.t.up()
        self.t.goto(self.configs["road_start_pos_x"], self.configs["road_start_pos_y"])

        # draw the stops
        for stop in self.game_board_data:
            self.stampStop(stop["stopType"],stop["isAboveRoad"],stop["hasSecondSpace"])
            self.t.setx(self.t.pos()[0]+self.configs["stop_spacing_dist"])

    # Logic for drawing the stops on the gameboard
    def stampStop(self, stop_type, is_above, is_two_player):
        # Set the color
        if(stop_type=="inn"):
            self.t.color('#B97A56')
            self.t.turtlesize(1.8,1.8,1)
            self.t.stamp()
            self.t.turtlesize(.8,.8,.5)
        elif(stop_type=="shop"):
            self.t.color('#FFFFFF')
        elif(stop_type=="temple"):
            self.t.color('#DF3922')
        elif(stop_type=="encounter"):
            self.t.color('#CD0984')
        elif(stop_type=="farm"):
            self.t.color('#E1C968')
        elif(stop_type=="bath"):
            self.t.color('#A9E0DC')
        elif(stop_type=="pano_g"):
            self.t.color('#A0D33B')
        elif(stop_type=="pano_w"):
            self.t.color('#9FB0AC')
        elif(stop_type=="pano_b"):
            self.t.color('#72C7EF')
        else:
            print("Error, wrong color for stampStop")
        # set the size
        if(stop_type!='inn'):
            returnPos = self.t.pos()
            # stamp on the road
            self.t.stamp()
            # draw a line
            self.t.down()
            if(is_above):
                self.t.forward(self.configs["stop_line_len"])
            else:
                self.t.backward(self.configs["stop_line_len"])
            self.t.stamp()
            if(OUTPUT_SPACE_COORDS):
                print(self.t.pos(), '\t- ', stop_type)
            # if two player stop, draw the second stop
            if(is_two_player):
                if(is_above):
                    self.t.forward(self.configs["stop_line_len"])
                else:
                    self.t.backward(self.configs["stop_line_len"])
                self.t.stamp()
                if(OUTPUT_SPACE_COORDS):
                    print(self.t.pos(), '\t- ', stop_type, '\t- 2')
            # return to the pos on the road
            self.t.up()
            self.t.goto(returnPos)

