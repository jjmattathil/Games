"""This is a python script for blackjack card game with one player and a computer dealer"""
suits=("Clubs","Hearts","Diamonds","Spades")
values={"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":(1,11)}
ranks=("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace")
from random import shuffle
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return (f'{self.suit} card of rank {self.rank}')

class Deck():
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
        shuffle(self.all_cards)

    def __len__(self):
        return len(self.all_cards)
    def pop_a_card(self):
        return self.all_cards.pop(0)
class PlayerAccount():
    def __init__(self,balance):
        self.balance=balance
    def credit_amount(self,amount):
        self.balance+=amount
    def withdraw_amount(self,amount):
        if (amount<=self.balance):
            self.balance-=amount
            return True
        else:
            print("Sufficient balance not available")
            return False
class Player():
    def __init__(self):
        self.my_cards=[]
        self.dis_sum=0
    def add_card(self,new_card):
        self.my_cards.append(new_card)
    def __len__(self):
        return len(self.my_cards)
class Dealer():
    def __init__(self):
        self.my_cards=[]
        self.dis_sum = 0
    def add_card(self,new_card):
        self.my_cards.append(new_card)
    def __len__(self):
        return len(self.my_cards)
def find_sum(name):
    name.dis_sum = 0
    for i in range(len(name)):
        if (name.my_cards[i].rank != "Ace"):
            name.dis_sum += name.my_cards[i].value
    for i in range(len(name)):
        if (name.my_cards[i].rank == "Ace"):
            if ((name.dis_sum+ 11)) < 21:
                name.dis_sum+= 11
            else:
                name.dis_sum += 1
    return name.dis_sum
def hit(name):
    if (name.dis_sum < 21):
        name.add_card(my_deck.pop_a_card())
        return True
    else:
        print("There is a bust")
        return False
def stay():
    pass
def anybody_wins(player,dealer,player_account):
    if (player.dis_sum == 21):
        print("Player wins")
        player_account.credit_amount(int(bet_amount) * 2)
        return True
    elif (player.dis_sum > 21):
        print("Dealer wins")
        return True
    elif (dealer.dis_sum > 21):
        print("Player wins")
        player_account.credit_amount(int(bet_amount) * 2)
    elif (dealer.dis_sum == 21):
        print("Dealer wins")
    return False

if __name__=="__main__":

    player_account=PlayerAccount(1000)
    new_round=True
    while new_round:
        print("Player balance is {}".format(player_account.balance))
        ##Start Betting
        while True:
            bet_amount = input("Enter bet amount: ")
            if bet_amount.isdigit():
                if player_account.withdraw_amount(int(bet_amount)):
                    break
        player = Player()
        dealer = Dealer()
        my_deck = Deck()
        for card in range(2):
            player.add_card(my_deck.pop_a_card())
            dealer.add_card(my_deck.pop_a_card())
        #Player sum
        print("Player Total is: {}".format(find_sum(player)))
        print("Dealer first card is: {}".format(dealer.my_cards[-1].value))
        if (len(player) == 2 and player.dis_sum == 21):
            print("BlackJack!!!!!!!!!!")
            print("Player wins!")
            player_account.credit_amount(int(bet_amount) * 2)
            game_on = False
            break
        game_on=True
        while game_on:
            #Player Always goes first
            hit_flag=True
            hit_stay=''
            while hit_stay not in ['h','s'] and hit_flag==True:
                hit_stay=input("Do you want a hit or stay? Enter 'h' or 's': ")
                if hit_stay=='h':
                    if hit(player):

                        print("Player took a new card and now the sum is {}".format(find_sum(player)))
                        if anybody_wins(player,dealer,player_account):
                            game_on = False
                            hit_flag=False
                            break
                    else:
                        if anybody_wins(player,dealer,player_account):
                            hit_flag = False
                            game_on = False
                            break
                else:
                    stay()
                    if len(dealer)>2 and len(player)>2:
                        if dealer.dis_sum == player.dis_sum:
                            print("Match on draw")
                            player_account.credit_amount(int(bet_amount) * 3 / 2)
                            game_on = False
                            break
                    #Dealer Sum
                    print("\n"*10)
                    print("Dealer Total is: {}".format(find_sum(dealer)))
                    if(dealer.dis_sum<player.dis_sum):
                        if hit(dealer):
                            print("Player Total is: {}".format(player.dis_sum))
                            print("Dealer took a new card and now the sum is {}".format(find_sum(dealer)))
                            if anybody_wins(player, dealer, player_account):
                                game_on = False
                                break
                        else:
                            if anybody_wins(player, dealer, player_account):
                                game_on = False
                                break
        user_ip=input("Do you want to start a new round? Enter 'y' or 'n': ")
        if(user_ip=='n'):
            new_round=False
            break
        else:
            new_round=True
            print("\n"*100)

