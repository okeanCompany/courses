capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}

# print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]

# print D
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])
