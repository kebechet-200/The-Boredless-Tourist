destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "São Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ["Erin Wilkes", "Shanghai, China", ["Historical site","art"]]

def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

test_destination_index = get_traveler_location(test_traveler)

attractions = [[] for i in range(5)]

def add_attraction(destination,attraction):
    try:
        destination_index = get_destination_index(destination)
        attractions_for_destination = attractions[destination_index].append(attraction)
    except ValueError:
        return

add_attraction("Los Angeles, USA", ["Venice Beach", ["beach"]])

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])


def find_attaction(destination,interests):
    destination_index = get_destination_index(destination)
    attactions_in_city = attractions[destination_index]
    attactions_with_interest = []

    for i in attactions_in_city:
        possible_attaction = i
        attactions_tags = i[1]

        for i in interests:
            if i in attactions_tags:
                attactions_with_interest.append(possible_attaction[0])

    return attactions_with_interest

def get_attactions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]

    traveler_attractions = find_attaction(traveler_destination,traveler_interests)

    interests_string = f"Hi {traveler[0]}, we think you'll like these places around: "

    for i in traveler_attractions:
        interests_string += f"{i}. "
        
smills_france = get_attactions_for_traveler(["Dereck Smill", "Paris, France", ['monument']])
print(smills_france)
