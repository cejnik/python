from instagram_data import data
import random

def account_generator(all_accounts):
    all_accounts = all_accounts[random.randint(0,len(all_accounts)-1)]
    return all_accounts


def printing_options(acc1, acc2):
    print(f"Porovnejte A: {acc1['name']},{acc1['description']} z {acc1['country']} ")
    print(f"Porovnejte B: {acc2['name']},{acc2['description']} z {acc2['country']} ")

def game ():
    account_1 = account_generator(data)
    account_2 = account_generator(data)
    right_answer = ""
    score = 0

    if account_1["name"] == account_2["name"]:
        account_2 = account_generator(data)
    
    while True:
        printing_options(account_1, account_2)
        user_answer = input("Kdo má více sledujících na instagramu? A nebo B? ")
        if account_1 == account_2:
            account_2 = account_generator(data)
        if account_1["follower_count"] > account_2["follower_count"]:
            right_answer = "A"
            account_1 = account_2
        else:
            right_answer = "B"
            account_2 = account_1

        if right_answer == user_answer:
            score += 1
            print(f"Uhádli jste, Vaše skóre je {score}")
            account_2 = account_generator(data)
        else:
            print(f"To je špatně. Vaše konečné skore je: {score}")
            break

game()












# acount_1 = data[random.randint(0,len(data)-1)]
# acount_2 = data[random.randint(0,len(data)-1)]
# print(acount_1["follower_count"])
# print(acount_2["follower_count"])
