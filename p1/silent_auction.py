from silent_action_logo import auction_logo
import os
print(auction_logo)

# naplnění dictionary nabízejícími
print("Vítejte v aplikaci tiché aukce")
bidders = {}
lets_continue = "ano"
while lets_continue == "ano":
    name = input("Jaké je Vaše jméno? \n")
    bid = int(input("Jaká je vaše nabídka v dolarech? \n"))
    bidders[name] = bid
    lets_continue = input("Jsou další nabízející? Napište ano nebo ne. ")
    if lets_continue == "ne":
        os.system("cls")
# print(bidders)
# Hledání nejvyšší nabídky
# highest_bid = 0
# winner = ""
# for key in bidders:
#     if bidders[key] > highest_bid:
#         highest_bid = bidders[key]
#         winner = key
  
# print(f"Vyhrál {winner} s nabídkou {highest_bid}")

def highest_bid(bidders_dictionary):
    highest_bid = 0
    winner = ""
    for key in bidders_dictionary:
        if bidders_dictionary[key] > highest_bid:
            highest_bid = bidders_dictionary[key]
            winner = key
    print(f"Vyhrál {winner} s nabídkou {highest_bid}")

highest_bid(bidders)