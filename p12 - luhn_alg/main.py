# card_number = '5011054488597827'
# card_number = card_number[::-1]


# sum_sude = 0
# for index in range(0,len(card_number),2):
#     sum_sude += (int(card_number[index]))


# sum_two_number_digits = 0
# outcome = 0
# sum_liche = 0
# for index in range(1, len(card_number),2):
#     new_number = int(card_number[index]) * 2
#     if new_number > 9:
#         two_digs_numbers = int(str(new_number)[0]) + int(str(new_number)[1])
#         # print(two_digs_numbers)
#         sum_two_number_digits += two_digs_numbers
#     else:
#         outcome += new_number
# final_number = outcome + sum_two_number_digits + sum_sude
# if final_number % 10 == 0:
#     print('Validní')
# print(final_number)
    
    
# Druhé řešení
# card_number = '5011054488597827'
# reverse_card_number = card_number[::-1]
# sum = 0
# for index, number in enumerate(reverse_card_number): #index(int) & number (str)
#     number = int(number)
#     if index % 2 == 1:
#         number *= 2
#         if number > 9:
#             number -= 9
    
#     sum += number

# if sum % 10 == 0:
#     print('Validní')
# else:
#     print('Nevalidní')

# Třetí řešení
# list_comprehension
card_number = '5011054488597827'
number = [int(one_number) for one_number in card_number]
sum_odd_numbers = sum(number[1::2])
sum_even_position = sum((one_number*2)%9 if one_number !=9 else 9 for one_number in number[::2])
if (sum_odd_numbers + sum_even_position) % 10 ==0:
    print("Karta je validní")
else:
    print('Karta je nevalidní')





    