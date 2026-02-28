# with open("input/general_letter.txt") as letter:
#     letter_content = letter.read()
# with open ("input/names.txt") as names:
#     names = names.readlines()
#     for one_name in names:
#         one_name = one_name.strip()
#         with open (f"output/invitation_for_{one_name}.txt", mode="w") as final_letter:
#             final_letter.write(letter_content.replace("[name]", one_name))
            
#         



with open ("input/general_letter.txt") as letter:
    letter_content = letter.read()

with open ("input/names.txt") as all_names:
    all_names = all_names.readlines()
    for one_name in all_names:
        one_name = one_name.strip()
        with open (f"output/invitation_{one_name}", mode = "w") as final_letter:
            final_letter.write(letter_content.replace("[name]", one_name))