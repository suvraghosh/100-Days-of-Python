# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(countries_visited,times_visited,cities_visited):
    new_country={}
    new_country["country"]=countries_visited
    new_country["visits"]=times_visited
    new_country["cities"]=cities_visited
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)