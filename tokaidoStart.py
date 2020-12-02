import json

class Strategy:
    sortedList = []
    def __init__(self, spacesDict):
        # Sort the spaces of the strategy highest to lowest
        highVal = 0
        highS = ''
        for i in range(9):
            print('i: ' + str(i))
            for s in spacesDict:
                print('s: ' + s)
                if int(spacesDict.get(s)) > highVal:
                    highVal = spacesDict.get(s)
                    highS = s
                    print('highVal: ' + highVal + ', highS: ' + highS)
            self.sortedList.append(highS)
            del spacesDict[highS]
            print(self.sortedList)
            highVal = 0
            highS = ''
        print("soting complete")
        print(self.sortedList)
                
            
info_list = dict()

# load and print the strats
with open('strats.json') as json_file:
    json_data = json.load(json_file)
    for s in json_data['strategies']:
        if s['name'] == 'all_panos':
        #print('Name: ' + s['name'])
            info_list = s['info']
        #for i in info_list:
            #print(i + ": " + info_list.get(i))


strat = Strategy(info_list)
