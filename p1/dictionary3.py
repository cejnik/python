students_results = {
  "Harry": 85,
  "Ron": 71,
  "Hermione": 98,
  "Draco": 69
}

# Stupnice
# 91 až 100 = "Excelentní"
# 81 až 90 = "Vynikající"
# 71 až 80 = "Splněno"
# méně jak 71 = "Nesplněno"

# Pokud není and, záleží na pořadí. Cyklus si bere hodnoty od vrchu.
description_result = {}
for key in students_results:
    # result = ""
    score = students_results [key]
    if score >90:
        description_result[key] = "Excelentní"
    elif score >80:
        description_result[key] = "Vynikající"
    elif score >70:
        description_result[key] = "Splněno"
    else:
        description_result[key] = "Nesplněno"
    # description_result[key] = result

print(description_result)