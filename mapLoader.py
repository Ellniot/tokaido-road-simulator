import json

TEST_LOAD_MAP_JSON = False

def loadMapJson():
    with open('FullBoardData.json') as json_file:
        try:
            data = json.load(json_file)
        except:
            data = {}
            print("ERROR: FILE NOT LOADED TO JSON")
        if TEST_LOAD_MAP_JSON:
            print("Length of JSON = ", len(data))
            print("1st object = ", data[0])
            print("1st object['stopType'] = ", data[0]['stopType'])


if TEST_LOAD_MAP_JSON:
    loadMapJson()