# nesting a dictionary inside a dictionary
travel_log = {
    "France" : {"Cities visited": ["Paris", "Bordeax", "Marsaille", "Calais", "Strasburg"], "total visits" : 10},
    "Spain" : {"Cities visited" : ["Barcelona", "Madrid", "San Sebastian"], "total visits" : 4},
}
# print(travel_log)

# nesting a dictionary inside a list
travel_log_2 = [
    {"country": "France", 
     "Cities visited": ["Paris", "Bordeax", "Marsaille", "Calais", "Strasburg"], 
     "total visits" : 10,},
    {"country": "Spain", 
     "Cities visited" : ["Barcelona", "Madrid", "San Sebastian"], 
     "total visits" : 4,},
]
# function to add new countries to log
def add_new_country(country_visited, tot_visits, cities):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = tot_visits
    new_country["cities"] = cities
    travel_log_2.append(new_country)

# travel_log_2 = [{country_name, visits, [city_list]}]

                

add_new_country("Russia", 2, ["Moscow", "St Petersburg"])
print(travel_log_2)
