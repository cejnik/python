# Nejvyšší skére v testu
# score = [98, 50, 25, 78, 92]
# print(max(score))
# print(min(score))

score = input("Zadejte jednotlivé skore studentu oddělených čárkou a mezerou\n")
score_list = score.split(", ")

score_list_number = []

for index in range(0, len(score_list)):
    score_list_number.append (int(score_list[index]))

maximum = 0
for one_number in score_list_number:
    if one_number > maximum:
        maximum = one_number

print(f"Maximum je {maximum}")
