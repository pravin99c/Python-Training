# Create a simulation program for Hot Potato Game.
# - At least one person must remove from each round.
# - Display name in the console that which user has a hot potato.
# - Each user holds a potato for random seconds between 0.1 to 3.0
# - Each round starts after 3 seconds of the previous elimination.
# - Each round stops at random seconds between 5 to 20.
# - Display the name of the winner.

from itertools import count
from os import remove
import time,random

list_name = ['Pravin','Aksh','Prachi','Kshitij','Komal']
remove_player = ""
print("**********         Strat Hot Potato Game               **********")
print("*******  List_of_player : ", list_name ," ********")
print()
print()
for i in range(len(list_name)-1):
    Second_first=0
    Second=random.randint(5,20)
    counter=0
    # Second_con=round(random.uniform(0.1,3.0),1)
    while Second_first <= Second:
        Second_con=round(random.uniform(0.1,3.0),1)
        Second_first += Second_con
        counter +=1
        if counter == len(list_name):
            counter = 0
        remove_player = list_name[counter]
    print("**********      Out Of Game = ",remove_player,"      **********")
    for i in range(3):
        print()
    list_name.remove(remove_player)
    time.sleep(3)
winner_plyer=list_name[0]
print("**********     Winner Player = ",winner_plyer,"      **********")
for i in range(3):
    print()
print("**********         End Hot Potato Game                           **********")
for i in range(3):
    print()