import random
from collections import Counter

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
        values = [2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'ACE']
        return [str(Card(value, color)) for value in values for color in colors]

class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = None
        self.order = list(enumerate([2,3,4,5,6,7,8,9,10,'J', 'Q', 'K', 'ACE']))
        self.rank = None

    def __repr__(self):
        return f'{self.name} has {self.chips} chips'

    def play_draw(self):
        game = Draw()
        game.deal(self)

        for _ in range(2):
            game.redraw(self)

        print(f'You have {self.hand}')

    def find_high_card(self):
        
        if self.hand == None:
            return 'Can not evaluate'
        else:
            Vals = [x.split()[0] for x in self.hand]            

        high_val = -1
        
        for card in Vals:
            for val in self.order:
                if card == val[1]:
                    if val[0]>high_val:
                        high_val= val[0]
                        high_card = card
                              
        return high_card
    
    # TODO
    # # Hand Evaluator
    # # Betting system
    
    def eval_hand(self):
                
        Low_Straight = False
        Straight = False
        Flush = False

        nums = set()
        suits = set()
    
        for Card in self.hand:
            nums.add(Card.split()[0])
            suits.add(Card.split()[1])
        
        # to compare to nums in situations
        Cards = [x.split()[0] for x in self.hand]

        #All straights, flushes, and straight flushes
        if len(nums)==len(self.hand):
            if len(suits)==1:
                Flush = True 
                        
            ordered = []
            for x in nums:
                for y in self.order:
                    if x == str(y[1]):
                        ordered.append(y[0])

            o = sorted(ordered)
            if o == [0,1,2,3,12]:
                Low_Straight = True
            if o[-1]-o[0]== len(self.hand)-1:
                Straight = True     

            if Straight==True and Flush == True:
                if o[-1]==12:
                    self.rank = 9
                    return f' You have a Royal Flush'
                else:
                    self.rank = 8
                    return f' You have a {self.find_high_card()} high straight flush'
            
            if Low_Straight ==True and Flush==True:
                self.rank = 8
                return 'You have a 5 high straight flush'
            if Flush ==True and Low_Straight == False and Straight==False:
                self.rank = 5    
                return f' You have a {self.find_high_card()} high flush'
            if Low_Straight == True and Flush == False:
                self.rank = 4
                return 'You have a 5 high straight'
            if Straight == True and Flush == False:
                self.rank = 4
                return f'You have a {self.find_high_card()} high straight'
            
            self.rank = 0
            return f'You have {self.find_high_card()} high'
        elif len(nums)==len(self.hand)-1:
            
            for card in nums:
                Cards.remove(card)

            self.rank = 1
            return f"You have a pair of {Cards[0]}'s"    
        elif len(nums)==len(self.hand)-2:
                        
            for card in nums:
                Cards.remove(card)

            if Cards[0]==Cards[1]:

                self.rank = 3
                return f"You have three {Cards[0]}'s" 
            else:
                self.rank = 2
                ordered = []
                for x in Cards:
                    for y in self.order:
                        if x == str(y[1]):
                            ordered.append(y[0])

                o = sorted(ordered, reverse=True)
                two_pair = []
                for val in o:
                    for x in self.order:
                        if val == x[0]:
                            two_pair.append(x[1])
                return f"You have {two_pair[0]}'s and {two_pair[1]}'s"            
        # full house
        elif len(nums)==len(self.hand)-3:
            for card in nums:
                Cards.remove(card)
            self.rank =6
            c = Counter(Cards)
            for k,v in c.items():
                if v == 2:
                    first = k
                elif v ==1:
                    second = k
            return f"You have a full house! {first}'s and {second}'s"         








        
        
        #2pair:len(s)==len(self.hand)-2
        #fullhouse:len(s)==len(self.hand-3)
        #3kind = len(self.hand-2)
        
        # TODO
        # 2 pair, 3 of a kind, full house

        #  
        # Pair
        # 2 Pair
        # 3 of a kind
        # straight
        # flush
        # Full house
        # 4 of a kind
        # straight flush
        # royal (straight) flush

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
            cards = ['0','1','2','3']
        elif Ace==True:
            cards = ['0','1','2','3','4']       
        can_exit = False
        
        while True:
            if can_exit ==True:
                break           

            while True:

                Count= input(f' You have {player.hand}, you can draw up to {int(cards[-1])} cards. How many cards would you like to draw?: ')
                
                if Count in cards:
                    Count = int(Count)                
                
                    can_exit = True
                    break

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
print(J.eval_hand())
