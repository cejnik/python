# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Moje řešení:
# def encode (message, shift_number):
#     shifted_text = ""
#     for one_letter in message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index + shift_number
#             if (new_index + index) > len(alphabet):
#                 shifted_text += alphabet[new_index - len(alphabet)]
#             else:
#                 shifted_text += alphabet[new_index]
#         else:
#             shifted_text += one_letter
#     print(f"Your encrypted text is {shifted_text}")

# def decode (encrypted_message, shift_number):
#     normal_text = ""
#     for one_letter in encrypted_message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index - shift_number
#             if index < shift_number:
#                 normal_text += alphabet[len(alphabet) - (shift_number - index)]
#             else:
#                 normal_text += alphabet[new_index]
#         else:
#             normal_text += one_letter
#     print(f"Your decrypted text is {normal_text}")

# # encode("martin", 5)
# # decode("rfwyns", 5)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encode(message, shift_number):
#     shifted_text = ""
#     for one_letter in message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index + shift_number
#             shifted_text += alphabet[new_index]
#         else:
#             shifted_text += one_letter
#     print(f"Your encrypted text is: {shifted_text}")

# def decode(encrypted_message, shift_number):
#     normal_text = ""
#     for one_letter in encrypted_message:
#         if one_letter != " ":
#             index = alphabet.index(one_letter)
#             new_index = index - shift_number
#             normal_text += alphabet[new_index]
#         else:
#             normal_text += one_letter
#     print(f"Your decrypted text is: {normal_text}")


def cipher (start_text, shift_number, direction):
    end_text = ""
    for one_letter in start_text:
        if one_letter != " ":
            index = alphabet.index(one_letter)
            if direction == "encode":
                new_index = index + shift_number
                end_text += alphabet[new_index]
            elif direction == "decode":
                new_index = index - shift_number
                end_text += alphabet[new_index]

        else:
            end_text += one_letter
    print(f"Your operation was {direction} and result is {end_text} ")

lets_continue = "yes"
while lets_continue == "yes":
    direction = input("Do you want to encode or decode your message? \n").lower()
    text = input("Write you message: \n").lower()
    shift = int(input("What shift do you want: \n"))
    # if direction == "encode":
    cipher(text, shift, direction)
    lets_continue = input("Do you want to continue? yes or no.")
    # elif direction =="decode":
    #     decode(text, shift)
    #     lets_continue = input("Do you want to continue? yes or no.")
    # else:
    #     print("Incorrect format of answer")
print("Thank you for usage our program.")
    




