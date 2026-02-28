travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    }
]

def add_country(country, visited_cities, visits):
    new_dictionary = {}
    new_dictionary["country"] = country
    new_dictionary["visited_cities"] = visited_cities
    new_dictionary["visits"] = visits
    travel_diary.append(new_dictionary)
 
add_country("Czechia", ["Pardubice", "Hradec Králové, Praha"], 2)
print(travel_diary[2]["visits"])
