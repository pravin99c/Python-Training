# Create class Cards with two list suits (Hearts, Diamonds, Clubs, Spades)
#  and  values (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K)

# -> Create a class deck. That contains a method to get a card set containing 52 elements.
# -> Create class shuffle. That contains two methods to shuffle given cards and remove/pick a single card.
# -> Create two objects of the above class as players. Each player pick/remove 5 cards from the shuffle cards. 
# Total points of both players and display name of winner player.


import random


class Cards():
    list_suits=['Hearts', 'Diamonds', 'Clubs', 'Spades']
    list_values=['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
class deck(Cards):
    def get_card(self):
        card_set=[]
        for i in Cards.list_suits:
            for j in Cards.list_values:
                card_set.append((i,j))
        return card_set
class Shaffle(deck):
    def shaffle_card(self):
        list_card=self.get_card()
        random.shuffle(list_card)
        return list_card
    def pick(self):
        list_card=self.shaffle_card()
        remove_player=[]
        first_line=0
        for i in range(5):
            card_pick=list_card[0]
            remove_player.append(card_pick)
            list_card.remove(card_pick)
        # print(remove_player)
        d={'A':13,'K':12,'Q':11,'J':10,10:9,9:8,8:7,7:6,6:5,5:4,4:3,3:2,2:1}
        for i in remove_player:
            first_card=i[1]
            for j in d:
                if first_card==j:
                    first_line += d[j]
        return first_line

player1=Shaffle()
player1.shaffle_card()
player1=player1.pick()
player2=Shaffle()
player2.shaffle_card()
player2=player2.pick()
# print(player1,player2)
if player1 > player2:
    print()
    print("Player 1 is Winner")
elif player1==player2:
    print()
    print("match draw ")
else:
    print()
    print("Player 2 is Winner ")