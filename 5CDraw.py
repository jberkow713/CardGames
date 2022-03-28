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
        values = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'Ace']
        return [str(Card(value, color)) for value in values for color in colors]

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = None

    def __repr__(self):
        return f'{self.name} has {self.chips} chips'


    def play_draw(self):
        game = Draw()
        game.deal(self)


        for i in range(2):
            game.redraw(self)

        print(f'You have {self.hand}')
    
    # def eval_hand(self):
        
        # ['8 D', 'Ace S', '3 S', 'K D', '3 C']
        
        # High Card no Pairs
        # Pair
        # 2 Pair
        # 3 of a kind
        # straight
        # flush
        # Full house
        # 4 of a kind
        # straight flush
        # royal (straight) flush




    # # TODO
    # # Hand Evaluator
    # # Betting system

class Draw:
    def __init__(self):
        self.deck = Deck().deck

    def deal(self, player):
        player.hand = random.sample(self.deck,5)
        for card in player.hand:
            self.deck.remove(card)
    
    def redraw(self, player):

        Ace= False    
        hand = player.hand
        for card in hand:
            if 'Ace' in card:
                Ace=True
                break
        if Ace==False:
            cards = 3
        elif Ace==True:
            cards = 4       
        can_exit = False
        
        while True:
            if can_exit ==True:
                break           

            Count= int(input(f' You have {player.hand}, you can draw up to {cards} cards. How many cards would you like to draw?: '))
            if Count <= cards:
                can_exit = True

                new_cards = random.sample(self.deck,Count)
                returned = []

                while Count >0:
                    available = input(f'Which of {player.hand} do you want to discard?')
                    if ' ' not in available:

                        for Card in player.hand:
                            card =Card.replace(' ', '')
                            if available.upper() == card:
                                returned.append(Card)
                                player.hand.remove(Card)
                                Count -=1
                    else:
                        card =available.upper()
                        if card in player.hand:

                            player.hand.remove(card)
                            returned.append(card)
                            Count -=1

                for card in returned:
                    self.deck.append(card)
                for card in new_cards:
                    player.hand.append(card)
                    self.deck.remove(card)

        print(f'You now have {player.hand}')

J = Player('Jesse', 100)
J.play_draw()