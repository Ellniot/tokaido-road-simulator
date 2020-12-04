# strat dictates the priority of each space with 10 being the highest
DEFAULT_STRAT = {
    "name": "closest",
      "info": {
        "encounters": 1,
        "pano_g": 1,
        "pano_w": 1,
        "pano_b": 1,
        "temple": 1,
        "shop": 1,
        "bath": 1,
        "farm": 1,
        "inn": 1
      }
}

class Player():
    name = ""
    strat = dict()
    victory_points = 0
    money = 0
    space = 0
    in_second_space = False
    position = (0,0)
    shopCards = []
    pano_g_cards = 0
    pano_w_cards = 0
    pano_b_cards = 0
    ability = ""
    def __init__(self, name, strat = DEFAULT_STRAT, ability = ""):
        self.name = name
        self.strat = strat
        self.ability = ability
    
    # space on gameboard getter and setter
    def get_space(self):
        return self.space
    
    def set_space(self, space_num, is_second_space, pos_x, pos_y):
        self.space = self.space_num
        self.is_second_space = is_second_space
        self.position = (pos_x, pos_y)
    
    # money adders and getters
    def get_money(self):
        return self.money

    def add_money(self, ammount):
        self.money = self.money + ammount

    def spend_money(self, ammount):
        if self.money < ammount:
            return "fail"
        else:
            return "success"

    # victory points adders and getters
    def add_victory_points(self, ammount):
        self.victory_points = self.victory_points + ammount
    
    def get_victory_points(self):
        return self.victory_points
    
    # pano card adders and getters
    def get_pano(self, type):
        if type == "g":
            return self.pano_g_cards
        elif type == "w":
            return self.pano_w_cards
        elif type == "b":
            return self.pano_b_cards
        else:
            print("GET_PANO TYPE ERROR, ASKED FOR TYPE \"", type, "\"")

    def is_pano_complete(self, type):
        if type == "g":
            return !(self.pano_g_cards < 3)
        elif type == "w":
            return !(self.pano_w_cards < 4)
        elif type == "b":
            return !(self.pano_b_cards < 5)
        else:
            print("GET_PANO TYPE ERROR, ASKED FOR TYPE \"", type, "\"")
    
    def add_pano(self, type):
        if self.is_pano_complete(type):
           print("ADD PANO ERROR: PANO ALREADY COMPLETE") 
        else:
            if type == "g":
                self.pano_g_cards = self.pano_g_cards + 1
            elif type == "w":
                self.pano_w_cards = self.pano_w_cards + 1
            elif type == "b":
                self.pano_b_cards = self.pano_b_cards + 1

    # shop cards adder (cards defined in separate file)
    def get_shop_cards(self):
        return self.shopCards
    
        # TODO this will have logic to determine the order of best shop cards to buy when at the shop
    def get_desired_shop_cards(self):
        return []

    def add_shop_card(self, shop_card):
        # TODO is this the correct syntax??
        self.shopCards.append(shop_card)