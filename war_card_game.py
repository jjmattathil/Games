""" This python script demonstrates WAR - card game"""
from war_lib import *

if __name__=="__main__":
    my_deck=Deck()
    player1=Player("jinu")
    player2=Player("dino")
    this_round = 0
    for i in range(52):
        new_card = my_deck.pop_card()
        if(i%2==0):
            player1.receive_card([new_card])
        else:
            player2.receive_card([new_card])
    game_on=True
    while game_on:
        this_round+=1
        print(f'The round is {this_round}')
        if (len(player1)==0):
            print("{} lost,{} wins the match with {} cards".format(player1.name,player2.name,len(player2)))
            break
        if (len(player2)==0):
            print("{} lost,{} wins the match with {} cards".format(player2.name,player1.name,len(player1)))
            break
        player1_cards=[]
        player2_cards = []
        player1_cards.append(player1.pop_player_card())
        player2_cards.append(player2.pop_player_card())
        war_on=True
        while war_on:
            if player1_cards[-1].value>player2_cards[-1].value:
                player1.receive_card(player1_cards+player2_cards)
                war_on=False
                break
            elif player2_cards[-1].value>player1_cards[-1].value:
                player2.receive_card(player1_cards+player2_cards)
                war_on=False
                break
            elif player2_cards[-1].value==player1_cards[-1].value:
                print("There is a war!!!!!!!!!!")
                if (len(player1) < 5):
                    print("{}  lost and has {} only cards,{} wins the match and has {} cards. {} cards on draw ".format(player1.name,len(player1),player2.name,len(player2),(len(player1_cards)+len(player2_cards))))
                    war_on=False
                    game_on=False
                    break
                if (len(player2) < 5):
                    print("{}  lost and has {} only cards,{} wins the match and has {} cards. {} cards on draw".format(player2.name,len(player2),player1.name,len(player1),(len(player1_cards)+len(player2_cards))))
                    war_on=False
                    game_on=False
                    break
                for i in range(5):
                    player1_cards.append(player1.pop_player_card())
                    player2_cards.append(player2.pop_player_card())
                    war_on=True

