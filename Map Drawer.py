import turtle
import json

# Debugging
OUTPUT_SPACE_COORDS = False
OUTPUT_LOAD_STRATS = False
OUTPUT_PLAYER_CREATION = False
OUTPUT_PLAYER_TURNS = True
OUTPUT_OPEN_SPACE_GEN = True

#road len = 918 = 17*54stops
ROAD_START_POS = (-530,0)
ROAD_END_POS = (530,0)
STOP_LINE_LEN = 40
STOP_SPACING_DIST = 20
roadmap = [['inn',False,False],['shop',True,True],['temple',False,False],['encounter',True,False],['pano_g',False,False],['bath',True,True],['pano_w',False,True],['farm', True, True],['shop',False,False],['temple',True,True],['encounter',False,False],['pano_b',True,True],['bath',True,False],['inn',False,False],['pano_b',False,False],['temple',True,False],['farm',False,True],['pano_g',True,True],['pano_w',False,True],['encounter',True,True],['temple',False,False],['bath',True,True],['pano_w',False,False],['pano_b',True,True],['shop',False,False],['farm',True,False],['inn',False,False],['pano_g',False,False],['shop',True,False],['encounter',False,True],['farm',True,False],['pano_w',False,True],['bath',True,False],['pano_b',False,True],['pano_g',True,False],['temple',False,True],['farm',True,True],['encounter',False,False],['pano_b',True,False],['shop',False,True],['inn',False,False],['bath',True,False],['temple',False,True],['encounter',True,False],['shop',False,True],['pano_b',True,False],['farm',False,True],['bath',True,True],['encounter',False,False],['pano_w',True,False],['pano_g',False,True],['pano_b',True,True],['shop',False,False],['inn',False,False]]
SPACES_COORDS_DICT = {'0':ROAD_START_POS}
SPACES_KEYS = []
STRATEGIES = [] # empty array of dicts

class Player:
    name = -1
    strat = dict()
    victory_points = 0
    money = 0
    space = 0
    position = (0,0)
    shopCards = []
    pano_g_cards = 0
    pano_w_cards = 0
    pano_b_cards = 0
    def __init__(self, playerNum, playerType, stratName='closest'):
        self.name = playerNum
        self.space = -1*playerNum
        self.position = SPACES_COORDS_DICT.get('0')
        for s in STRATEGIES:
            if OUTPUT_PLAYER_CREATION:
                # Print the {name:{strat ranks}}
                print(s)
                # Print name
                print(list(s)[0])
            currentStratName = list(s)[0]
            if currentStratName == stratName:
                self.strat = s.get(currentStratName)
        if OUTPUT_PLAYER_CREATION:
            print('Player Created')

    # where openSpaces is [0,1,1.5,...] - space indecies
    def takeTurn(self, openSpaces):
        if OUTPUT_PLAYER_TURNS:
            print('Player 1 - moving to: ' + destinationName)
        desiredSpaceRank = 10
        space_found = False # keep looping until a choice is made
        while(not space_found):            
            # Iterate through the strat high->low
            for sp_rnk in self.strat:
                if strat.get(sp_rnk) == desiredSpaceRank:
                    # Iterate through the available spaces close->far
                    for i in range(openSpaces):
                        if roadmap[openSpaces[i]][0] == sp_rnk:
                            space_found = True
                            self.space = self.space + i + 1 # b/c it starts form 0
                            self.position = SPACES_COORDS_DICT.get(self.space)
                            
                
            
    def getSpace(self):
        return self.space

    
def LoadSpacesCoords():
    with open('spacesDict.csv', 'r') as inf:
        for line in inf:
            split = line.split(',')
            SPACES_COORDS_DICT.update({split[0]:split[1]})
    keys = list(SPACES_COORDS_DICT.keys())
    for k in keys:
        SPACES_KEYS.append(k)
    print(str(SPACES_KEYS))
    print(type(SPACES_KEYS))
    # print the dict
    #for s in SPACES_COORDS_DICT:
    #    print(s + ': ' + str(SPACES_COORDS_DICT.get(s)))

def LoadJson():
    if(OUTPUT_LOAD_STRATS):
        print('loading strategies')
    with open('strats.json') as json_file:
        json_data = json.load(json_file)
        for s in json_data['strategies']:
            if(OUTPUT_LOAD_STRATS):
                print('adding strategy: ' + s['name'])
            STRATEGIES.append({s['name']:s['info']})

def stampStop(stopType, isAbove, isTwoPlayer, t):
    # Set the color
    if(stopType=="inn"):
        t.color('#B97A56')
        t.turtlesize(1.8,1.8,1)
        t.stamp()
        t.turtlesize(.8,.8,.5)
    elif(stopType=="shop"):
        t.color('#FFFFFF')
    elif(stopType=="temple"):
        t.color('#DF3922')
    elif(stopType=="encounter"):
        t.color('#CD0984')
    elif(stopType=="farm"):
        t.color('#E1C968')
    elif(stopType=="bath"):
        t.color('#A9E0DC')
    elif(stopType=="pano_g"):
        t.color('#A0D33B')
    elif(stopType=="pano_w"):
        t.color('#9FB0AC')
    elif(stopType=="pano_b"):
        t.color('#72C7EF')
    else:
        print("Error, wrong color for stampStop")
    # set the size
    if(stopType!='inn'):
        returnPos = t.pos()
        # stamp on the road
        t.stamp()
        # draw a line
        t.down()
        if(isAbove):
            t.forward(STOP_LINE_LEN)
        else:
            t.backward(STOP_LINE_LEN)
        t.stamp()
        if(OUTPUT_SPACE_COORDS):
            print(t.pos(), '\t- ', stopType)
        # if two player stop, draw the second stop
        if(isTwoPlayer):
            if(isAbove):
                t.forward(STOP_LINE_LEN)
            else:
                t.backward(STOP_LINE_LEN)
            t.stamp()
            if(OUTPUT_SPACE_COORDS):
                print(t.pos(), '\t- ', stopType, '\t- 2')
        # return to the pos on the road
        t.up()
        t.goto(returnPos)

def DrawGameBoard():
    wn = turtle.Screen()
    wn.screensize(1000,250)
    wn.bgcolor('#E8EEE8')
    t = turtle.Turtle()
    t.speed(0)
    t.up()
    t.pensize(5)
    t.left(90)  # make the turtle face up
    t.shape("circle")
    t.color('#AAAAAA')
    t.goto(ROAD_START_POS)
    # draw the background road
    t.down()
    t.goto(ROAD_END_POS)
    t.up()
    t.goto(ROAD_START_POS)
    for stop in roadmap:
        stampStop(stop[0],stop[1],stop[2],t)
        t.setx(t.pos()[0]+STOP_SPACING_DIST)
        
    t.ht()

# this check could be more efficient if it used an array that updated each move
def FindBackPlayer(p_list):
    # set the last space to positive b/c the starting
    #   order will be 0,-1,-2, etc.
    last_space_number = 1
    last_player = p_list[0]
    for p in p_list:
        if p.getSpace() < last_space_number:
            last_player = p
            last_space_number = p.getSpace()
    return p
        
def GetOpenSpaces(p_list):
    inn_locations = [1,14,27,41,54]
    past_inn_index = 0
    current_locations = []
    occupied_inn = 10 # something out of index of the inns
    second_inn = 10
    open_spaces = []
    for p in p_list:
        current_locations.append(p.getSpace())
        # check if a player is between inns, this tells which spaces to use
        if p.getSpace() not in inn_locations:
            # see which inn was just left
            for i in inn_locations:
                if i < p.getSpace():
                    past_inn_index = i
                else:
                    break
            break
        # player is at an inn
        else:
            # check if an inn is occupied
            if occupied_inn == 10:
                # set the current inn to this player's location
                occupied_inn = p.getSpace()
            # check if the player is at the same inn as the other player
            elif occupied_inn == p.getSpace():
                # do nothing
                break
            # the player is at a different inn from the other player,
            # but we'll check anyways
            elif occupied_inn != p.getSpace():
                second_inn = p.getSpace()
            else:
                print('Error, this case shouldnt be reached')
    if OUTPUT_OPEN_SPACE_GEN:
        print('Current player locations: ' + str(current_locations))
        if occupied_inn != 10:
            print('Inn at ' + inn_locations[occupied_inn] + ' occupied')
            if second_inn != 10:
                print('Second inn at ' + inn_locations[second_inn] + ' occupied')
    # see if anyone is past each inn
    occupied_inn = 10
    for i in range(len(inn_locations)):
        for l in current_locations:
            if l > inn_locations[i]:
                break; # break out of this inner for loop, increment outer loop
            else:
                next_inn_index = i+1
    if OUTPUT_OPEN_SPACE_GEN:
        print('Next inn: ' + str(inn_locations[past_inn_index+1]))
    # create a list of stop indexes between the inns, include the ending inn
    for i in range(inn_locations[past_inn_index], inn_locations[past_inn_index+1]+1):
        open_spaces.append(i)
        # see if there is a second spot on the stop
        i_plus = i + 0.5
        # if the half space is in the dictionary, add it
        if str(i_plus) in SPACES_KEYS:
            open_spaces.append(i_plus)
    if OUTPUT_OPEN_SPACE_GEN:
        print('List of spaces before next inn (inclusive): ' + str(open_spaces))
    # remove the spaces where players are
    for p in p_list:
        # check if the players are negative b/c it is the start of the game
        if p.getSpace() > 0:
            open_spaces.remove(p.getSpace())
    if OUTPUT_OPEN_SPACE_GEN:
        print('List of available spaces before next inn (inclusive): ' + str(open_spaces))
        
                
        
    
def SimGame(numPlayers, playerInfo):
# player info is a list of (playerType, strat) tuples
    playerTurtleList = []
    #DrawGameBoard()
    # confirm that len(playerInfo == numPlayers)
    if numPlayers != len(playerInfo):
        print('ERROR: Player Info List does not match number of players!')
        return 0
    playerList = [Player(i,playerInfo[i][0],playerInfo[i][1]) for i in range(numPlayers)]
    gameover = False
    # main game loop
    while(not gameover):
        # find the furthest back player
        currentPlayer = FindBackPlayer(playerList)
        currentPlayer.takeTurn(GetOpenSpaces(playerList))
        gameover = True
        
        

def Main():
    LoadSpacesCoords()
    LoadJson()
    if OUTPUT_LOAD_STRATS:
        # STRATEGIES is list of dicts
        for i in STRATEGIES:
            # i is dict {name:{dict of strat info}}
            for j in i:
                # j is {spaceName:rank}
                print(j)
                print(i.get(j))
    playerInfo = [['artist','closest'],['orphan','closest'],['priest','closest']]
    SimGame(3,playerInfo)
    

Main()
