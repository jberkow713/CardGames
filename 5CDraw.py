import random

class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        

    def __repr__(self):
        return f'{self.value} {self.color}'    

class Deck:
    def __init__(self):
        self.deck = self.create_deck()

    def create_deck(self):

        colors = ['H', 'D', 'S', 'C']
        values = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'A']
        return [Card(value, color) for value in values for color in colors]

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = None

    def __repr__(self):
        return f'{self.name} has {self.chips} chips'    
class Draw:
    def __init__(self):
        self.deck = Deck().deck

    def deal(self, player):
        

        hand = []
        for i in range(5):
            while True:

                card = self.deck[random.randint(0,len(self.deck)-1)]
                if card not in hand:
                    hand.append(card)
                    break
                            
        player.hand = hand         


J = Player('Jesse', 100)
print(J)

game = Draw()
game.deal(J)
print(J.hand)