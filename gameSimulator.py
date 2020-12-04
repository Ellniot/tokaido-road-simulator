from mapLoader import load_map_json
from window_controler import Gameboard
from time import sleep

VERBOSE_DEBUGGING = True

def main():
    if VERBOSE_DEBUGGING:
        print("Running gameSimulator.py:main()")
    
    # TODO: Load Configs
    configs = {
        "useGameGUI": True,
        "game_win_size_x": 1000,
        "game_win_size_y": 250,
        "game_win_bg_color": '#E8EEE8',
        "road_start_pos_x": -530,
        "road_start_pos_y": 0,
        "road_end_pos_x": 530,
        "road_end_pos_y": 0,
        "stop_spacing_dist": 20,
        "stop_line_len": 40
    }
    if VERBOSE_DEBUGGING:
        print("Configs loaded")

    # TODO Move to window_controller.py if it's only used there
    default_map_data = load_map_json()
    if VERBOSE_DEBUGGING:
        print("\tLoaded default map data")
        print("\tMap length = ", len(default_map_data))
        print("\tFirst stop on map = ", default_map_data[0])

    if configs["useGameGUI"]:
        gameboard = Gameboard(default_map_data, configs)
    


    


main()