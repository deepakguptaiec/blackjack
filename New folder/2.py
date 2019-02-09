#print("a is greater") if(int(input("enter the number of a ="))>int(input("enter the number of b ="))) else  print("b is greater ")


'''
list1=[25,6,4,8,7,9,5]
for i in list1:
    if i==int(input("enter the number = ")):
        print("the number is found")
        break
else:
    print("the number is not found")
'''




import random
dealer_card=[]
player_card=[]

while len(dealer_card) != 2:
    dealer_card.append(random.randint(1,11))
    if len(dealer_card) ==2:
        print("dealer has X &",dealer_card[1])


while len(player_card) !=2:
    player_card.append(random.randint(1,11))
    if len(player_card)==2:
        print("player_card has :",player_card)



if sum(dealer_card)==21:
    print("dealer has 21 and wins!")
elif sum(dealer_card) > 21:
    print("dealer has busted!")

while sum(player_card) < 21:
    action_taken=str(input("do you to stay or hit? "))
    if action_taken=="hit":
        player_card.append(random.randint(1,11))
        print("you now have a total of"   + str(sum(player_card)) +   "from these cards ",player_card)
    else:
        print("the dealer has a total of"   + str(sum(dealer_card)) +   "with",dealer_card)
        print("you have a total of "   + str(sum(player_card)) +   "with",player_card)
        if sum(dealer_card)>sum(player_card):
            print("dealer wins!")
        else:
            print("you win!")
            break


if sum(player_card)>21:
    print("you BUSTED! Dealer wins.")
elif sum(player_card)==21:
    print("you have BLACKJACK! You Win! 21")


