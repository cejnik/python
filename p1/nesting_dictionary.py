# Nesting
# cities = {
#     "Spain": "Madrid",
#     "France": "Paris"
# }
# print(cities["Spain"])

# List v dictionary
# travel_diary = {
#     "Spain": ["Madrid", "Leon", "Valencia"],
#     "France": ["Paris", "Nice", "Rennes"]
# }

# print(travel_diary["France"][0])

# Dictionary v dictionary
# travel_diary = {
#     "Spain":{"visited_cities" : ["Madrid", "Leon", "Valencia"],
#              "non_visited_cities" : ["Palma", "Toledo", "Alicante"]
#             },
#     "France":{"visited_cities" : ["Paris", "Nice", "Rennes"],
#             "non_visited_cities" : ["Avignon", "Nice", "Dijon"]
#             },
# }

# print(travel_diary["Spain"]["visited_cities"][1])

# Dictionary v listu
travel_diary = [
    {"country": "Spain",
     "visited_cities" : ["Madrid", "Leon", "Valencia"],
     "non_visited_cities" : ["Palma", "Toledo", "Alicante"],
     },
    {"country": "France",
     "visited_cities" : ["Paris", "Nice", "Rennes"],
     "non_visited_cities" : ["Avignon", "Nice", "Dijon"],
     },
]

print(travel_diary[1]["non_visited_cities"][2])