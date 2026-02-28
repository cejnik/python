score = input("Zadejte čísla oddělené mezerou a čárkou? \n")
score_list = score.split(", ")
score_list_empty = []
for index in range (0, len(score_list)):
    score_list_empty.append(int(score_list[index]))
minimum = max(score_list_empty)
for one_number in score_list_empty:
    if one_number < minimum:
        minimum = one_number
print(f"Minimální hodnota ze seznamu je {minimum}")