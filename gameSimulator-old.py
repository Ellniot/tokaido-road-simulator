#import tkinter
import Tkinter as tk

STRAT_LIST = ['templeDons','pano_all']
STRAT_LIST_DESCS = []
PLAYER_LIST = ['Artist', 'Messenger', 'Ronin', 'Functionary', 'Orphan', 'Old Man', 'Geisha', 'Priest', 'Entertainer', 'Merchant']

# player class with type, strategy, and counters for each card and money
class Player():
    def __init__(self, pType, pStrat):
        self.pType = pType
        self.pStrat = pStrat
        self.points = 0
        self.money = 0
        self.templeDons = 0
        self.pano_g = 0
        self.pano_w = 0
        self.pano_b = 0
    def addPoints(self, numOfPoints):
        self.points = self.points + numOfPoints
    def getPoints(self):
        return self.points
    def donate(self, ammount):
        if ammount > self.money:
            print('Not enough money to make that donation.')
            return 0
        else:
            self.money = self.money - ammount
            self.templeDons = self.templeDons + ammount
    def getDonationCount(self):
        return self.templeDons
    def recieveMoney(self, ammount):
        self.money = self.money + ammount
    def spendMoney(self, ammount):
        self.money = self.money - ammount

# global game instance vars
playerList = {}

def RunSim():
    # open turtle window with the board
    print("Running the sim")
    return 0

# update the options win based on number of players selected
def UpdatePCount(win, count):
    print("win = ", win)
    win.destroy()
    newWin = tk.Tk()
    #OptionsGUI(newWin, count)

# open a gui and get user option inputs
def OptionsGUI(optionsWin, pNum):
    optionsWin.__init__(None)
    optionsWin.title=("Tokaido Road Simulator")
    optionsWin.geometry('600x400')

    # create the variables for the options
    pCount = tk.IntVar(optionsWin)
    pCountList = {'4','3','5'}
    pCount.set(pNum)
    pTypeList = [tk.StringVar(optionsWin) for i in range(pNum)]
    pStratList = [tk.StringVar(optionsWin) for i in range(pNum)]

    # add the options GUI elements
    #   make the title and player number selector
    title_lbl = tk.Label(optionsWin, text='Tokaido Road').pack()
    #title_lbl.grid(row=0)
    #title_lbl.pack()
    pCount_drpdn = tk.OptionMenu(optionsWin, pCount, *pCountList)
    #pCount_drpdn.grid(row=1)
    pCount_drpdn.pack()
    #   make the player options panes based on pNum
    pOptions_pn = tk.PanedWindow(optionsWin)
#TODO: make labels 'player 1', 'player 2'...
    player_drpdnList = [tk.OptionMenu(optionsWin, pTypeList[i], *PLAYER_LIST) for i in range(pNum)]
    strat_drpdnList = [tk.OptionMenu(optionsWin, pStratList[i], *STRAT_LIST) for i in range(pNum)]
    pOptionPair_pnList = [tk.PanedWindow(optionsWin, orient='vertical') for i in range(pNum)]
    for i in range(pNum):
        pOptionPair_pnList[i].add(player_drpdnList[i])
        pOptionPair_pnList[i].add(strat_drpdnList[i])
        pOptions_pn.add(pOptionPair_pnList[i])
    #pOptions_pn.grid(row=2)
    pOptions_pn.pack()
    #   make the next button
    next_bt = tk.Button(optionsWin, text='Next', command=lambda : OpenStratSelector(pCount.get()))
    #next_bt.grid(row=3)
    next_bt.pack()
    # add the player options to the options pane
    #for i in range(pNum):
    #    
    #    pOptions.add()

    # function links for when option values change
    pCount.trace('w', UpdatePCount(optionsWin, pCount.get()))

    optionsWin.mainloop()
    
    
def LoadStratDescs():
    # load the global strategy descriptions
    print('Strategy descriptions loaded')
    return 0

def Main():
    LoadStratDescs()
    mainWin = tk.Tk()
    #OptionsGUI(mainWin, 3)
    return 0

Main()
