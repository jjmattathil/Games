from random import shuffle
suits=("Hearts","Clubs","Diamonds","Spades")
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
values_dict={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":11,"Queen":12,"King":13,"Ace":14}
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values_dict[rank]

    def __str__(self):
        return f'This is a {self.rank} {self.suit} card.'
class Deck():
    def __init__(self):
        self.all_cards=[]
        for i in suits:
            for j in ranks:
                create_a_card=Card(i,j)
                self.all_cards.append(create_a_card)
        shuffle(self.all_cards)

    def __str__(self):
        return f'This consists of 14 cards of 4 suits'

    def pop_card(self):
        return self.all_cards.pop()
class Player():
    def __init__(self,name):
        self.name=name
        self.my_hand_card=[]
    def receive_card(self,new_cards):
        self.my_hand_card.extend(new_cards)
    def pop_player_card(self):
        return self.my_hand_card.pop(0)
    def __len__(self):
        return len(self.my_hand_card)
